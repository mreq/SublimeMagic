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
        replacement = self.spell.get('args').get('replacement')

        clipboard = sublime.get_clipboard()
        replacement = replacement.replace('$clipboard', clipboard)

        cursor_position = replacement.find('$cursor')
        if cursor_position is not -1:
            replacement = replacement.replace('$cursor', '')

        region = sublime.Region(start, end)

        self.view.replace(self.edit, region, replacement)

        if cursor_position != -1:
            new_cursor_position = start + cursor_position
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(new_cursor_position))
            if self.view.settings().get('vintage'):
                self.view.run_command("_enter_insert_mode")
