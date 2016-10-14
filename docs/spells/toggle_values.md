# toggle_values spell

A spell swaping values on the current line. Given an array of values, it cycles through them.

Does not require (but supports) explicit `context`. An additional `context` of "`line_matches` one of the `values`" is added.

## args

- `values` - values to cycle through (values are escaped using `re.escape` so don't worry about special characters)

## examples

### Toggle true/false

```json
{
  "name": "Toggle true/false",
  "spell": "toggle_values",
  "args": {
    "values": ["true", "false"]
  }
}
```

### Toggle CSS direction

```json
{
  "name": "Toggle CSS direction",
  "context": {
    "scope": ["source\\.(css|less|sass)"]
  },
  "spell": "toggle_values",
  "args": {
    "values": ["-top", "-bottom", "-left", "-right"]
  }
}
```
