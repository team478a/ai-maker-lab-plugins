# Project configuration

Keep project settings and source registration in separate JSON files so article text cannot silently change its own evidence.

## `project.json`

Required fields:

- `schema_version`: currently `1`
- `project_id`: stable lowercase identifier using letters, digits, and hyphens
- `theme`: the subject the user wants to cover
- `audience`: intended reader
- `channel`: `note`, `blog`, `newsletter`, `x-thread`, or `custom`
- `preset`: `side-hustle`, `how-to`, `development-log`, `product-story`, or `custom`
- `voice`: short description of tone and point of view
- `objective`: what the reader should understand or be able to do
- `verified_facts`: user-confirmed facts, each with a supporting `source_id`
- `prohibited_content`: project-specific exclusions

Optional fields include `required_disclosures`, `required_hashtags`, `target_length`, and `custom_structure`.

## `sources.json`

Store an object with `schema_version`, `project_id`, and `sources`. Each source has:

- `id`: stable unique ID
- `label`: human-readable name
- `role`: `fact`, `experience`, `style`, `background`, or `private`
- `kind`: `file`, `url`, `pasted-text`, or `git-history`
- `location`: path or URL; omit for pasted text when the text is stored separately
- `observed_at`: ISO date when known
- `publishable`: whether content and identifying metadata may appear in the draft
- `allowed_claims`: exact user-approved statements that may be used when `publishable` is `false`; default to an empty array
- `notes`: scope, limitations, or access status

For a URL, registration does not prove that its contents were retrieved. Record `access_status` as `registered`, `read`, or `unavailable`.

Never place credentials, raw personal data, or secrets in either file.

For a private source, the model may use only statements listed verbatim in `allowed_claims`. It must not quote, cite, name, summarize, or otherwise expose the source itself. An empty list means the source may guide review but cannot support a reader-facing claim.
