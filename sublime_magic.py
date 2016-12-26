import re
import sublime
import sublime_plugin
from .messenger import messenger
from .spells import *
from .context import context


class SublimeMagic(sublime_plugin.TextCommand):

    def run(self, edit):
        self.edit = edit
        self.known_spells = [
            'replace_text',
            'perform_line_regex',
            'toggle_values',
            'sublime_command'
        ]

        self.get_user_spells()
        self.find_first_matching_user_spell()

        if self.spell is None:
            self.message('No spell found.')
        else:
            try:
                self.cast_spell()
            except NotImplementedError as e:
                self.message(str(e))

    def get_user_spells(self):
        self.magic_settings = sublime.load_settings(
            'SublimeMagic.sublime-settings')
        self.user_spells = self.magic_settings.get('spells')

    def find_first_matching_user_spell(self):
        self.spell = None
        for spell in self.user_spells:
            if context.check(self.view, spell):
                self.spell = spell
                break

    def message(self, message):
        if not hasattr(self, 'messenger'):
            self.messenger = messenger.Messenger()
        self.messenger.message(self.view, '★ ' + message, True)

    def spell_to_class(self, string):
        return ''.join(x.capitalize() or '_' for x in string.split('_'))

    def cast_spell(self):
        spell_name = self.spell.get('spell')
        if not spell_name in self.known_spells:
            raise NotImplementedError('Unknown spell: ' + spell_name)
        try:
            spell_class = eval(
                spell_name +
                '.' +
                self.spell_to_class(spell_name) +
                'Spell')
            spell_class = spell_class(self.edit, self.view, self.spell)
            spell_class.cast()
            name = self.spell.get('name', None)
            if not name:
                name = spell_name
            self.message('Casted ' + name)
        except AttributeError as e:
            return self.message('Invalid args for "' +
                                spell_name + '". ' + str(e))
