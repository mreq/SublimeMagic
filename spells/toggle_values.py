import re
import sublime

from .magic_spell import MagicSpell


class ToggleValuesSpell(MagicSpell):
    required_args = ['values']

    def cast(self):
        self.values = self.spell.get('args').get('values')
        escaped_values = [re.escape(val) for val in self.values]
        pattern = '(' + '|'.join(escaped_values) + ')'

        sel = self.view.sel()[0]
        line = self.view.line(sel.a)
        line_text = self.view.substr(line)
        new_line_text = re.sub(pattern, self.replace, line_text)

        return self.view.replace(self.edit, line, new_line_text)

    def replace(self, matchobj):
        index = self.values.index(matchobj.group(0)) + 1
        if index > len(self.values) - 1:
            index = 0
        return self.values[index]
