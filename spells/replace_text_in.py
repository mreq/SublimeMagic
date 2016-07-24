import re
import sublime

from .magic_spell import MagicSpell

class ReplaceTextInSpell(MagicSpell):
    required_args = ['delimiter', 'replacement']

    def cast(self):
        self.delimiter = re.compile(self.spell.get('args').get('delimiter'))
        self.replacement = self.spell.get('args').get('replacement')
        print(self.replacement)
        if self.replacement == '$clipboard':
            self.replacement = sublime.get_clipboard()
        start = self.find_previous_delimiter()
        if start:
            end = self.find_next_delimiter()
            if end:
                return self.replace(start, end)

    def find_previous_delimiter(self):
        start = self.view.sel()[0].a
        line = self.view.line(start)
        found = None

        while start > line.a:
            region = sublime.Region(start - 1, start)
            if self.delimiter.match(self.view.substr(region)):
                found = start
                break
            start -= 1

        return found

    def find_next_delimiter(self):
        start = self.view.sel()[0].b
        line = self.view.line(start)
        found = None

        while start < line.b:
            region = sublime.Region(start, start + 1)
            if self.delimiter.match(self.view.substr(region)):
                found = start
                break
            start += 1

        return found

    def replace(self, start, end):
        region = sublime.Region(start, end)
        self.view.replace(self.edit, region, self.replacement)
