import re
import sublime

from .magic_spell import MagicSpell
from ..utils import utils


class ReplaceTextSpell(MagicSpell):
    required_args = ['where', 'delimiter', 'replacement']

    def cast(self):
        where = self.spell.get('args').get('where')
        delimiter = self.spell.get('args').get('delimiter')
        delimiter_length = len(delimiter)
        re_delimiter = re.compile(delimiter)

        self.replacement = self.spell.get('args').get('replacement')
        if self.replacement == '$clipboard':
            self.replacement = sublime.get_clipboard()

        for sel in self.view.sel():
            line = self.view.line(sel.a)

            if where == 'inside':
                start = utils.find_previous_delimiter(
                    self.view, line, re_delimiter, sel.a)

                if start:
                    end = utils.find_next_delimiter(
                        self.view, line, re_delimiter, delimiter_length, sel.b)
                    if end:
                        self.replace(start, end)

            elif where == 'after':
                start = utils.find_next_delimiter(
                    self.view, line, re_delimiter, delimiter_length, line.a)
                if start:
                    start = start + delimiter_length
                    end = line.b
                    if end:
                        return self.replace(start, end)

            else:
                raise AttributeError('Unknown value for "where": ' + where)

    def replace(self, start, end):
        region = sublime.Region(start, end)
        self.view.replace(self.edit, region, self.replacement)
