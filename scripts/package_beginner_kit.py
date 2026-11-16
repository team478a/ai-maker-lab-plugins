#!/usr/bin/env python3
"""Build a beginner-friendly downloadable local marketplace ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
DOWNLOAD = ROOT / "download"
COPY_ENTRIES = (".agents", "plugins", "docs", "examples", "LICENSE", "README.md", "SUPPORT.md")
MARKETPLACE_NAME = "ai-maker-lab-download"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def replace_placeholders(source: Path, destination: Path, version: str) -> None:
    text = source.read_text(encoding="utf-8").replace("__VERSION__", version)
    destination.write_text(text, encoding="utf-8", newline="\n")


def copy_distribution(bundle: Path) -> None:
    for name in COPY_ENTRIES:
        source = ROOT / name
        destination = bundle / name
        if source.is_dir():
            shutil.copytree(source, destination)
        elif source.is_file():
            shutil.copy2(source, destination)
        else:
            fail(f"required distribution entry is missing: {name}")


def configure_local_marketplace(bundle: Path) -> None:
    path = bundle / ".agents" / "plugins" / "marketplace.json"
    marketplace = json.loads(path.read_text(encoding="utf-8"))
    marketplace["name"] = MARKETPLACE_NAME
    marketplace["interface"]["displayName"] = "AI MAKER LAB Download"
    path.write_text(
        json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def validate_bundle(bundle: Path) -> None:
    validator = ROOT / "scripts" / "validate_distribution.py"
    environment = os.environ.copy()
    environment["AI_MAKER_LAB_MARKETPLACE_NAME"] = MARKETPLACE_NAME
    result = subprocess.run(
        [sys.executable, str(validator), "--root", str(bundle)],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        fail(result.stderr.strip() or result.stdout.strip())


def create_zip(bundle: Path, output: Path) -> None:
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(bundle.rglob("*")):
            if not path.is_file() or path.is_symlink():
                continue
            relative = Path(bundle.name) / path.relative_to(bundle)
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            mode = 0o755 if path.name == "install-macos-linux.sh" else 0o644
            info.external_attr = mode << 16
            archive.writestr(info, path.read_bytes())


def validate_zip(output: Path, bundle_name: str) -> None:
    with zipfile.ZipFile(output) as archive:
        names = archive.namelist()
        for name in names:
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or not path.parts or path.parts[0] != bundle_name:
                fail(f"unsafe ZIP entry: {name}")
        required = {
            f"{bundle_name}/START_HERE.md",
            f"{bundle_name}/START_HERE.html",
            f"{bundle_name}/install-windows.cmd",
            f"{bundle_name}/install-macos-linux.sh",
            f"{bundle_name}/.agents/plugins/marketplace.json",
            f"{bundle_name}/plugins/source-backed-article-studio/plugin.json",
        }
        missing = sorted(required - set(names))
        if missing:
            fail(f"download ZIP is missing required files: {', '.join(missing)}")

        marketplace = json.loads(
            archive.read(f"{bundle_name}/.agents/plugins/marketplace.json").decode("utf-8")
        )
        if marketplace.get("name") != MARKETPLACE_NAME:
            fail("download ZIP has an unexpected marketplace name")
        for relative in ("START_HERE.md", "START_HERE.html", "install-windows.cmd", "install-macos-linux.sh"):
            text = archive.read(f"{bundle_name}/{relative}").decode("utf-8")
            if "__VERSION__" in text:
                fail(f"unreplaced version placeholder in {relative}")
        installers = "\n".join(
            archive.read(f"{bundle_name}/{relative}").decode("utf-8").lower()
            for relative in ("install-windows.cmd", "install-macos-linux.sh")
        )
        for forbidden in ("sudo ", "runas", "openai_api_key", "sk-"):
            if forbidden in installers:
                fail(f"installer contains forbidden privileged or secret pattern: {forbidden}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    plugin = json.loads((ROOT / "plugins" / "source-backed-article-studio" / "plugin.json").read_text(encoding="utf-8"))
    version = plugin["version"]
    bundle_name = f"source-article-studio-starter-{version}"
    output = output_dir / f"{bundle_name}.zip"

    with tempfile.TemporaryDirectory(prefix="source-article-studio-starter-") as temporary:
        bundle = Path(temporary) / bundle_name
        bundle.mkdir()
        copy_distribution(bundle)
        configure_local_marketplace(bundle)
        for name in ("START_HERE.md", "START_HERE.html", "install-windows.cmd", "install-macos-linux.sh"):
            replace_placeholders(DOWNLOAD / name, bundle / name, version)
        (bundle / "VERSION.txt").write_text(f"{version}\n", encoding="ascii", newline="\n")
        validate_bundle(bundle)
        create_zip(bundle, output)
        validate_zip(output, bundle_name)

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    checksum = output.with_suffix(output.suffix + ".sha256")
    checksum.write_text(f"{digest}  {output.name}\n", encoding="ascii", newline="\n")
    print(f"Created {output} with SHA-256 {digest}")


if __name__ == "__main__":
    main()
