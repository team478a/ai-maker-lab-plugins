#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

printf '\nSource Article Studio __VERSION__ をCodexへ追加します。\n'
printf '管理者権限、APIキー、パスワードは要求しません。\n\n'

if ! command -v codex >/dev/null 2>&1; then
  printf '%s\n' 'Codex CLIが見つかりません。'
  printf '%s\n' '先にCodexを利用できるPC環境を準備してください。'
  printf '%s\n' 'https://developers.openai.com/codex/cli/'
  exit 1
fi

codex plugin remove source-backed-article-studio@ai-maker-lab-download >/dev/null 2>&1 || true
codex plugin marketplace remove ai-maker-lab-download >/dev/null 2>&1 || true
codex plugin marketplace add "$ROOT"
codex plugin add source-backed-article-studio@ai-maker-lab-download

printf '\nインストールが完了しました。Codexを再起動してください。\n'
codex plugin list
