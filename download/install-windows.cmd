@echo off
setlocal
chcp 65001 >nul
title Source Article Studio Installer

echo.
echo Source Article Studio __VERSION__ をCodexへ追加します。
echo 管理者権限、APIキー、パスワードは要求しません。
echo.

where codex >nul 2>&1
if errorlevel 1 goto codex_missing

codex plugin remove source-backed-article-studio@ai-maker-lab-download >nul 2>&1
codex plugin marketplace remove ai-maker-lab-download >nul 2>&1

codex plugin marketplace add "%~dp0"
if errorlevel 1 goto install_failed

codex plugin add source-backed-article-studio@ai-maker-lab-download
if errorlevel 1 goto install_failed

echo.
echo インストールが完了しました。Codexを再起動してください。
codex plugin list
echo.
pause
exit /b 0

:codex_missing
echo Codex CLIが見つかりません。
echo 先にCodexを利用できるPC環境を準備し、もう一度実行してください。
echo https://developers.openai.com/codex/cli/
pause
exit /b 1

:install_failed
echo.
echo インストールに失敗しました。START_HERE.mdの「困ったとき」を確認してください。
pause
exit /b 1
