# Source Article Studio ダウンロード版

このZIPは、Source Article StudioをCodexへ追加する初心者向けスターターキットです。

## 最初に確認

- Pluginは無料です。
- Codex本体を使えるPC環境が別途必要です。Codex側の利用条件や契約が適用される場合があります。
- noteへの自動投稿、予約、決済は行いません。
- インストール用スクリプトは管理者権限、APIキー、パスワードを要求しません。

## Windows

1. ZIPを右クリックして「すべて展開」を選びます。
2. 展開したフォルダの`install-windows.cmd`をダブルクリックします。
3. Windowsの警告が出た場合は無理に回避せず、ファイルをテキストエディタで確認してください。
4. 完了後にCodexを再起動します。

## macOS / Linux

ターミナルで展開したフォルダへ移動し、次を実行します。

```bash
sh install-macos-linux.sh
```

## 最初の依頼例

> 初心者向けに記事を作りたいです。読者と媒体を決め、使ってよい資料の登録から始めてください。

次に資料を登録してから依頼します。

> 登録した資料だけに基づいてnote記事の下書きを作り、未確認事項と根拠の一覧も示してください。

詳しい操作は`docs/JAPANESE_FREE_GUIDE.md`、完成例は`examples/beginner-note/`を確認してください。

## 更新

新しいダウンロード版ZIPを入手し、別のフォルダへ展開してインストール用スクリプトを再実行します。スクリプトは`ai-maker-lab-download`から導入した旧版だけを置き換えます。作成済みの記事プロジェクトは削除しません。

## 困ったとき

- 「Codex CLIが見つかりません」と表示された場合、Codexの準備が必要です。
- 公開IssueへAPIキー、個人情報、非公開資料、未公開原稿を貼らないでください。
- サポート: <https://github.com/team478a/ai-maker-lab-plugins/issues>

このキットのバージョン: `__VERSION__`
