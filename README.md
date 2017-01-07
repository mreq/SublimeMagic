# ★ SublimeMagic

A magic command for sublime. Create a spellbook, cast spells on your code, make magic happen.

## What?

SublimeMagic provides a `sublime_magic` command, which looks through user-defined actions and performs the first matching one.

## Use the spell hotkey!

Default keybind is `alt + spacebar` but you can set your own. To use the plugin, you have to bind the `sublime_magic` command.

Regular example:

```json
{
  "keys": ["ctrl+,"],
  "command": "sublime_magic"
}
```

Vintageous example:

```json
{
  "keys": [" ", " "],
  "command": "sublime_magic",
  "context": [{ "key": "vi_command_mode_aware" }]
}
```


## Create your spellbook!

The spellbook (your sublime-settings file) consists of a single `spells` array containing the user-defined spells:

```json
{
  "spells": []
}
```

The spells are iterated one-by-one and the first one matching the `context` conditions is casted. When there's no spell matching, nothing happens. When there are multiple matching spells, only the top-most one is performed.

## Spell

Each spell consists of the following required fields:

- `name` is the human readable name of your spell
- `spell` is the spell code, see ["Available spells" for a list of spells](#available-spells)
- `args` specific to the selected spell

Spells can be limited by settings a `context` (similar to key bindings, though not using the same syntax). Known context keys:

- `scope` - an array of required scope names (using regexp) - all patterns must match 
- `line_matches` - an array of patterns that the current line must match
- `selection_empty` - when `true`, some text has to be selected; when `false`, there must be no selection
- `selection_matches` - an array of patterns that the currently selected text must match
- need more? - make an issue, or even better a PR :)

### Spell example

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

## Available spells

- [replace_text](docs/spells/replace_text.md)
- [perform_line_regex](docs/spells/perform_line_regex.md)
- [toggle_values](docs/spells/toggle_values.md)
- [sublime_command](docs/spells/sublime_command.md)
- more to come - make a PR :)

## Example spellbook

Have a nice spellbook? Create a pull request and let me add a link here!

Spellbooks:
+ [mreq](https://github.com/mreq/dotfiles/blob/master/subl/Packages/User/SublimeMagic.sublime-settings)

A simple example:

```json
{
  "spells": [
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
    },
    {
      "name": "Replace double quoted content with clipboard",
      "context": {
        "scope": ["string\\.quoted\\.double"]
      },
      "spell": "replace_text",
      "args": {
        "where": "inside",
        "delimiter": "\"",
        "replacement": "$clipboard"
      }
    },
    {
      "name": "Replace content after colon with clipboard",
      "context": {
        "line_matches": [": "]
      },
      "spell": "replace_text",
      "args": {
        "where": "after",
        "delimiter": ": ",
        "replacement": "$clipboard"
      }
    }
  ]
}
```
