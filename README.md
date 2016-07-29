# ★ SublimeMagic

A magic command for sublime. Create a spellbook, cast spells on your code, make magic happen.

## What?

SublimeMagic provides a `sublime_magic` command, which looks through user-defined actions and performs the first matching one.

## Set your spell hotkey!

The plugin comes without default key bindings. To use the plugin, you have to bind the `sublime_magic` command.

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
- `spell` is the spell code, see see [Spells](#spells) for a list of spells
- `args` specific to the selected spell

Spells can be limited by settings a `context` (similar to key bindings, though not using the same syntax). Known context keys:

- `scope` - an array of required scope names (using regexp) - all patterns must match 
- `line_matches` - an array of patterns that the current line must match
- more to come - make a PR :)

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
- more to come - make a PR :)

## Example spellbook

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
