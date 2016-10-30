import re
import sublime

from .magic_spell import MagicSpell


class PerformLineRegexSpell(MagicSpell):
    required_args = ['pattern', 'replacement']

    def cast(self):
        pattern = re.compile(self.spell.get('args').get('pattern'))
        replacement = self.spell.get('args').get('replacement')
        sel = self.view.sel()[0]
        line = self.view.line(sel.a)

        if replacement == '$clipboard':
            replacement = sublime.get_clipboard()

        line_text = self.view.substr(line)
        new_line_text = re.sub(pattern, "%s" % replacement, line_text)

        return self.view.replace(self.edit, line, new_line_text)
