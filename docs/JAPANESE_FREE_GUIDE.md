# Source Article Studio｜日本語・無料導入ガイド

> AI MAKER LABの無料記事下書き作成Pluginです。2026-11-16時点の公開版`0.2.2`に合わせています。

## できること

- 記事テーマ、読者、媒体、目的を整理する。
- 事実、体験、文体、背景、非公開資料を分けて登録する。
- 登録した資料に基づくMarkdown下書きと、根拠manifestを作る。
- 未確認事項と公開前の確認項目を残す。

noteへの投稿、予約、決済、SNS投稿は行いません。生成物は必ず下書きとして保存されます。

## 利用条件

Plugin自体はMIT Licenseで無料配布され、Plugin専用のAPIキー、独自課金、専用サーバーはありません。ただしCodexを使える環境が必要で、Codex側の利用条件や契約が別途適用される場合があります。「Pluginが無料」と「利用環境を含むすべての費用が必ず無料」は同じ意味ではありません。

## 動作確認の範囲

- Codex CLI: Public Gitマーケットプレイスからの導入、更新、記事プロジェクト設定、Markdownとmanifestの生成を確認済み。
- Codexデスクトップ: Pluginの導入状態はCLIで確認済み。Plugins Directoryのロゴや説明の画面表示は利用者による目視確認が必要。
- ChatGPTやnote: このコマンドで直接インストールするものではない。

## インストール

Codex CLIが使えるPCのターミナルで実行します。

```bash
codex plugin marketplace add team478a/ai-maker-lab-plugins --ref main
codex plugin add source-backed-article-studio@ai-maker-lab
codex plugin list
```

一覧で`source-backed-article-studio@ai-maker-lab`が`installed, enabled`と表示されることを確認します。Codexデスクトップを併用する場合は、コマンド実行後にアプリを再起動します。

## 初めての記事下書き

### 1. テーマと読者を伝える

Codexで作業フォルダを開き、次の例を自分のテーマへ置き換えて依頼します。

> 初心者向けに、ベランダで育てるハーブの記録記事を作りたいです。読者は初めて栽培する人、媒体はnoteです。まず記事プロジェクトを設定してください。

### 2. 使用してよい資料を登録する

自分で確認した資料だけを渡し、事実、体験、文体、背景のどれかを伝えます。非公開資料は、そのまま公開してよい内容だけを明示してください。

> この栽培メモは自分の体験です。日付と作業内容は記事に使えますが、氏名と住所は使わないでください。未確認の効果は事実として書かないでください。

URLを登録しただけでは、そのページを読んだ証明にはなりません。取得できた資料と未取得の資料を区別します。

### 3. 下書きを作る

> 登録した資料だけに基づいてnote記事の下書きを作ってください。未確認事項と、事実ごとの根拠をmanifestへ残してください。

通常は記事プロジェクト内に`project.json`、`sources.json`、`drafts/<記事ID>.md`、`drafts/<記事ID>.manifest.json`が作られます。保存先は作業環境と依頼内容により変わるため、完了時に表示されるパスを確認してください。

完全な例は[初心者向けサンプル](../examples/beginner-note/README.md)で確認できます。

## noteへ貼り付ける前に

- Markdown本文を読み、見出し、改行、タイトルを調整する。
- manifestを見て、各事実に根拠があるか確認する。
- 引用、著作権、個人情報、PR表示、最新情報を確認する。
- 未確認の実績、売上、効果、利用者の感想を追加しない。
- noteへの貼り付けと公開は自分で行う。

## 更新

```bash
codex plugin marketplace upgrade ai-maker-lab
codex plugin add source-backed-article-studio@ai-maker-lab
codex plugin list
```

更新後に表示されるversionを確認します。既存の記事プロジェクトは削除せず、必要なら先にバックアップしてください。

## 困ったとき

- Pluginが見つからない: マーケットプレイス追加コマンドと`--ref main`を確認する。
- 更新されない: `marketplace upgrade`後にPlugin追加コマンドを再実行し、一覧のversionを確認する。
- 資料が使われない: `sources.json`の`access_status`、`publishable`、役割を確認する。
- 非公開資料がある: 生データを公開Issueへ貼らず、再現用の架空データへ置き換える。

## ライセンス・利用条件・サポート

- ライセンス: [MIT License](../LICENSE)
- Privacy Policy: [Plugin Privacy Policy](../plugins/source-backed-article-studio/legal/PRIVACY.md)
- Terms of Use: [Plugin Terms of Use](../plugins/source-backed-article-studio/legal/TERMS.md)
- サポート: [GitHub Issues](https://github.com/team478a/ai-maker-lab-plugins/issues)

公開IssueにはAPIキー、認証情報、個人情報、非公開資料、未公開原稿を記載しないでください。
