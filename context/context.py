import re


def check_scope(current_scope, target_scopes):
    valid = True
    for target_scope in target_scopes:
        if not re.search(target_scope, current_scope):
            valid = False
            break
    return valid


def check_line_matches(line_text, target_parts):
    valid = True
    for target_part in target_parts:
        if not re.search(target_part, line_text):
            valid = False
            break
    return valid


def check(view, spell):
    valid = True

    for sel in view.sel():
        line = view.line(sel.a)
        line_text = view.substr(line)
        view_scope = view.scope_name(sel.a)

        context = spell.get('context', {'scope': [], 'line_matches': []})
        spell_scope = context.get('scope', [])
        line_matches = context.get('line_matches', [])
        values = spell.get('args', {'values': None}).get('values', None)

        if values:
            escaped_values = [re.escape(val) for val in values]
            line_matches.append('(' + '|'.join(escaped_values) + ')')

        valid = check_scope(view_scope, spell_scope)

        if not valid:
            break

        valid = check_line_matches(line_text, line_matches)

        if not valid:
            break

    return valid
