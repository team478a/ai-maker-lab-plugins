# AI MAKER LAB Plugins

AI MAKER LABが提供するChatGPT / Codex向けPluginの配布用マーケットプレイスです。

## Source Article Studio

テーマ、読者、媒体、参照資料を設定し、根拠manifest付きのMarkdown記事下書きを作ります。

- APIキーや外部サーバーは不要
- 事実、体験、文体、背景、非公開資料を区別
- 非公開資料は明示的に許可した文だけを使用
- noteやWordPressへの投稿、予約、決済は行わない

## インストール

Codex CLIで次を実行します。

```bash
codex plugin marketplace add team478a/ai-maker-lab-plugins --ref main
codex plugin add source-backed-article-studio@ai-maker-lab
```

Codexデスクトップを利用する場合は、コマンド実行後にアプリを再起動し、Plugins Directoryで`AI MAKER LAB`を確認してください。

## 更新

```bash
codex plugin marketplace upgrade ai-maker-lab
codex plugin add source-backed-article-studio@ai-maker-lab
```

## データと公開

Pluginは独自サーバーへ記事データを送信しません。作成したファイルは利用者の作業環境に保存されます。詳しくはPlugin内の`legal/PRIVACY.md`を確認してください。

生成物は下書きです。事実、著作権、個人情報、広告表示、媒体設定を人が確認してから利用してください。

## ライセンス

PluginはMIT Licenseで配布します。著作権表示とライセンス文を維持すれば、利用、改変、再配布、商用利用が可能です。
