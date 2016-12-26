# sublime_command spell

A spell for running a sublime command.

## args

- `command` - command to be run
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
