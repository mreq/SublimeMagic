import re


def check_scope(current_scope, target_scopes):
    valid = True
    for target_scope in target_scopes:
        if not re.search(target_scope, current_scope):
            valid = False
            break
    return valid


def check_matches(text, target_parts):
    valid = True
    for target_part in target_parts:
        if not re.search(target_part, text):
            valid = False
            break
    return valid


def check_selection_empty(should_be_empty, sel):
    if should_be_empty:
        return sel.a is sel.b
    else:
        return sel.a is not sel.b


def check(view, spell):
    valid = True

    for sel in view.sel():
        context = spell.get('context', {
            'scope': [], 'line_matches': [], 'selection_matches': [],
            'selection_empty': None
        })

        spell_scope = context.get('scope', [])
        view_scope = view.scope_name(sel.a)
        valid = check_scope(view_scope, spell_scope)
        if not valid:
            break

        line = view.line(sel.a)
        line_text = view.substr(line)
        line_matches = context.get('line_matches', [])
        values = spell.get('args', {'values': None}).get('values', None)
        if values:
            escaped_values = [re.escape(val) for val in values]
            line_matches.append('(' + '|'.join(escaped_values) + ')')
        valid = check_matches(line_text, line_matches)
        if not valid:
            break

        selection_empty = context.get('selection_empty', None)
        if selection_empty is not None:
            valid = check_selection_empty(selection_empty, sel)
            if not valid:
                break

        selection_matches = context.get('selection_matches', [])
        selection_text = view.substr(sel)
        valid = check_matches(selection_text, selection_matches)
        if not valid:
            break

    return valid
