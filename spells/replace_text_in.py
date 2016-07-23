from . import magic_spell

class ReplaceTextInSpell(magic_spell.MagicSpell):
    required_args = ['delimiter', 'replacement']

    def cast(self):
        print(self.spell)
