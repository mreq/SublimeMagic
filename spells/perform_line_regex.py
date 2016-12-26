import re
import sublime

from .magic_spell import MagicSpell


class PerformLineRegexSpell(MagicSpell):
    required_args = ['pattern', 'replacement']

    def cast(self):
        pattern = re.compile(self.spell.get('args').get('pattern'))

        replacement = self.spell.get('args').get('replacement')
        if replacement == '$clipboard':
            replacement = sublime.get_clipboard()

        for sel in self.view.sel():
            line = self.view.line(sel.a)

            line_text = self.view.substr(line)
            new_line_text = re.sub(pattern, "%s" % replacement, line_text)

            self.view.replace(self.edit, line, new_line_text)
