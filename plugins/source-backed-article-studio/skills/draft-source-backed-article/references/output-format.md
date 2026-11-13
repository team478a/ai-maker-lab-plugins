# Output contract

Write two files under `drafts/` using the same article ID.

## `<article-id>.md`

Use this structure unless the selected channel or the user requires another:

```markdown
---
article_id: <id>
status: draft
generated_at: <ISO timestamp>
project_id: <project id>
---

# <selected title>

> タイトル候補: ... / ... / ...

<introduction and headed body>

## 公開前に確認すること

- [ ] <human review item>

<hashtags when appropriate>
```

Do not place internal-only source paths or evidence details in the article.

## `<article-id>.manifest.json`

Include:

- `schema_version`, `article_id`, `project_id`, `generated_at`, and `status: "draft"`
- `theme`, `source_ids`, and `source_revisions`
- `claims`: each factual claim, supporting source IDs, and confidence (`verified` or `review`)
- `blocked_findings` and `review_required`
- `content_sha256` when the environment can calculate it; otherwise set it to `null` and add a review item

If the same project, theme, and source revisions already have a draft manifest, update only when the user requests regeneration; otherwise point to the existing draft.
