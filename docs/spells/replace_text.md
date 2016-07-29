# replace_text spell

A spell for replacing text inside/after delimiters. 

## args

- `delimiter` - regexp pattern to be matched
- `replacement` - text used for replacement - when `$clipboard`, the clipboard content is used
- `where`
  - `inside` - replace text inside/between the delimiters
  - `after` - replace text after the delimiter

## examples

### Replace content of single quotes with the clipboard content

```json
{
  "name": "Replace single quoted content with clipboard",
  "context": {
    "scope": ["string\\.quoted\\.single"]
  },
  "spell": "replace_text",
  "args": {
    "where": "inside",
    "delimiter": "'",
    "replacement": "$clipboard"
  }
}
```

### Remove content after the first colon

```json
{
  "name": "Remove content after colon",
  "context": {
    "line_matches": [": "]
  },
  "spell": "replace_text",
  "args": {
    "where": "after",
    "delimiter": ":",
    "replacement": ""
  }
}
```
