import re
import sublime

from .magic_spell import MagicSpell


class ReplaceTextSpell(MagicSpell):
    required_args = ['where', 'delimiter', 'replacement']

    def cast(self):
        where = self.spell.get('args').get('where')
        self.delimiter_length = len(self.spell.get('args').get('delimiter'))
        self.delimiter = re.compile(self.spell.get('args').get('delimiter'))
        self.replacement = self.spell.get('args').get('replacement')
        self.sel = self.view.sel()[0]
        self.line = self.view.line(self.sel.a)

        if self.replacement == '$clipboard':
            self.replacement = sublime.get_clipboard()

        if where == 'inside':
            start = self.find_previous_delimiter(self.sel.a)
            if start:
                end = self.find_next_delimiter(self.sel.b)
                if end:
                    return self.replace(start, end)
        elif where == 'after':
            start = self.find_first_delimiter_in_line()
            if start:
                start = start + self.delimiter_length
                end = self.end_of_line()
                if end:
                    return self.replace(start, end)
        else:
            raise AttributeError('Unknown value for "where": ' + where)

    def find_previous_delimiter(self, start):
        found = None

        while start > self.line.a and start > 0:
            region = sublime.Region(start - 1, start)
            if self.delimiter.match(self.view.substr(region)):
                found = start
                break
            start -= 1

        return found

    def find_next_delimiter(self, start):
        found = None

        while start < self.line.b and start < 999999:
            region = sublime.Region(start, start + self.delimiter_length)
            if self.delimiter.match(self.view.substr(region)):
                found = start
                break
            start += 1

        return found

    def find_first_delimiter_in_line(self):
        return self.find_next_delimiter(self.line.a)

    def replace(self, start, end):
        region = sublime.Region(start, end)
        self.view.replace(self.edit, region, self.replacement)

    def end_of_line(self):
        return self.line.b
