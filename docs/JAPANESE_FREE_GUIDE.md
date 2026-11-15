# Source Article Studio｜日本語・無料導入ガイド

> AI MAKER LAB の無料記事下書き作成Pluginです。2026-11-16時点の公開版 `0.2.2` に合わせた案内です。

## 何ができる？
- 記事テーマ・読み手・媒体を設定して、資料に基づくMarkdown記事の**下書き**を作成する。
- 「事実」「体験」「文体」「背景」「非公開資料」を分けて管理し、根拠の一覧と確認事項も出力する。
- noteへの直接投稿、予約投稿、記事販売、購入者分析、SNS投稿は**行わない**。
- このPlugin自体の追加APIキー、独自課金、専用サーバーは不要。**Codexの利用環境・契約が別途必要**な場合がある。

## 対象者
- noteの記事を、自分で確認した事実や経験を使って下書きしたい人
- 複雑なプロンプトを毎回書き直したくない人
- 生成記事に使った情報源や確認事項を残したい人

## 動作確認済みの導入方法：Codex CLI
事前にCodex CLIが使用できる環境を用意してください。端末（ターミナル）で以下を実行します。

```bash
codex plugin marketplace add team478a/ai-maker-lab-plugins --ref main
codex plugin add source-backed-article-studio@ai-maker-lab
```

プロジェクトをCodexで開いたら、最初に次のように依頼します。

> このテーマの記事を作りたいです。読者と媒体を決め、資料の登録から始めてください。

次に、自分が使ってよい資料・自分で確かめた事実・経験を入力して、こう依頼します。

> 登録した資料に基づいてnoteの記事下書きを作り、未確認事項と根拠の一覧も示してください。

生成されたMarkdownを確認・編集し、ご自身のnote記事として利用してください。

## 更新
```bash
codex plugin marketplace upgrade ai-maker-lab
codex plugin add source-backed-article-studio@ai-maker-lab
```

## 初心者向けの注意
- このコマンドはCodex CLI用です。**ChatGPTアプリやnoteにそのままインストールできるという案内ではありません。**
- Codexデスクトップの画面表示は公開前の最終目視確認が残っています。公式Plugin Directoryへの掲載を確認したものではありません。
- 資料を登録しただけで内容が真実と保証されるわけではありません。引用、事実関係、著作権、個人情報、PR表示は公開前に確認してください。
- 「AIが自動で収益を発生させる」「完全自動投稿ができる」とは説明しません。

## 関連する別ツール（開発中）
AI MAKER LABでは、noteのURLからTikTok・Instagram・X向けの宣伝用動画と投稿文を作る**note集客動画メーカー**も企画中です。こちらは未配布・未実装であり、このPluginには含まれません。

## サポート・ライセンス
- バグ報告：<https://github.com/team478a/ai-maker-lab-plugins/issues>
- プライバシー：<https://github.com/team478a/ai-maker-lab-plugins/blob/main/plugins/source-backed-article-studio/legal/PRIVACY.md>
- 利用条件：<https://github.com/team478a/ai-maker-lab-plugins/blob/main/plugins/source-backed-article-studio/legal/TERMS.md>
- ライセンス：MIT（リポジトリの `LICENSE` を参照）
- AI MAKER LAB：<https://note.com/ai_maker_lab>

## 公開前に自分たちで再確認すること
- 少なくとも1台のクリーンなCodex CLI環境で導入からMarkdown生成まで再確認する
- README・Plugin version・導入コマンドの整合を確認する
- Codexデスクトップを利用者に案内する場合は、その画面での目視確認を済ませる
- note告知記事で「無料」「APIキー不要」の条件と、Codex本体が必要である点を同じ目立ち方で記載する
