import re

class ContextChecker(object):
    def __init__(self, view):
        self.view = view
        self.sel = self.view.sel()[0]
        self.line = self.view.line(self.sel.a)
        self.line_text = self.view.substr(self.line)
        self.scope_name = self.view.scope_name(self.sel.a)

    def check(self, spell):
        context = spell.get('context', { 'scope': [], 'line_matches': [] })
        scope = context.get('scope', [])
        line_matches = context.get('line_matches', [])
        valid = self.check_scope(scope)
        if not valid:
            return False
        valid = self.check_line_matches(line_matches)
        return valid

    def check_scope(self, target_scopes):
        is_valid = True
        for target_scope in target_scopes:
            if not re.search(target_scope, self.scope_name):
                is_valid = False
                break
        return is_valid

    def check_line_matches(self, target_parts):
        is_valid = True
        for target_part in target_parts:
            if not re.search(target_part, self.line_text):
                is_valid = False
                break
        return is_valid
