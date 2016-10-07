# perform_line_regex spell

A spell for running a `re.sub` on the current line.

## args

- `pattern` - regexp pattern 
- `replacement` - replacement (i.e. `repl`) - when `$clipboard`, the clipboard content is used

## examples

### Strip extra whitespace

```json
{
  "name": "Strip extra whitespace",
  "context": {
    "line_matches": ["\\S\\s\\s+"]
  },
  "spell": "perform_line_regex",
  "args": {
    "pattern": "(\\S)(\\s)\\s+",
    "replacement": "\\1\\2"
  }
}
```

### Add space to array

```json
{
  "name": "Add space to array",
  "context": {
    "line_matches": ["\\[.+\\]"]
  },
  "spell": "perform_line_regex",
  "args": {
    "pattern": "\\[(.+)\\]",
    "replacement": "[ \\1 ]"
  }
}
```
