# perform_line_regex spell

A spell for running any sublime command.

## args

- `command` - regexp pattern 
- `args` - arguments for the command

## examples

```json
{
  "name": "Add blank line after",
  "context": {},
  "spell": "sublime_command",
  "args": {
    "command": "run_macro_file",
    "args": {
      "file": "res://Packages/Default/Add Line.sublime-macro"
    }
  }
}
```
