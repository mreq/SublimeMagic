import re
import sublime
import sublime_plugin
from . import sublime_magic_messenger
from .spells import *

class SublimeMagic(sublime_plugin.TextCommand):
    def run(self, edit):
        self.edit = edit
        self.get_known_spells()
        self.get_defined_spells()
        self.get_scope()
        self.find_first_matching_spell()
        if self.spell is None:
            self.message('No spell found.')
        else:
            try:
                self.cast_spell()
            except NotImplementedError as e:
                self.message(str(e))

    def get_known_spells(self):
        # TODO: can we do this better?
        self.known_spells = []
        for name, val in globals().items():
            if hasattr(val, '__name__'):
                if 'SublimeMagic.spells' in val.__name__:
                    self.known_spells.append(name)

    def get_defined_spells(self):
        self.magic_settings = sublime.load_settings('SublimeMagic.sublime-settings')
        self.spells = self.magic_settings.get('spells')

    def find_first_matching_spell(self):
        self.spell = None
        for spell in self.spells:
            if self.context_check(spell.get('scope')):
                self.spell = spell
                break

    def message(self, message):
        if not hasattr(self, 'messenger'):
            self.messenger = sublime_magic_messenger.SublimeMagicMessenger()
        self.messenger.message(self.view, '★ ' + message, True)

    def get_scope(self):
        sel = self.view.sel()[0]
        line = self.view.line(sel)
        self.scope_name = self.view.scope_name(sel.a)

    def context_check(self, target_scopes):
        is_valid = True
        for target_scope in target_scopes:
            if not re.search(target_scope, self.scope_name):
                is_valid = False
                break
        return is_valid

    def spell_to_class(self, string):
        return ''.join(x.capitalize() or '_' for x in string.split('_'))

    def cast_spell(self):
        spell_name = self.spell.get('spell')
        if not spell_name in self.known_spells:
            raise NotImplementedError('Unknown spell: ' + spell_name)
        try:
            spell_fn = eval(spell_name + '.' + self.spell_to_class(spell_name) + 'Spell')
            spell_fn = spell_fn(self.edit, self.view, self.spell)
        except AttributeError as e:
            return self.message('Invalid args for "' + spell_name + '". ' + str(e))
        spell_fn.cast()
