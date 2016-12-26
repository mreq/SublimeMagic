import sublime

from .magic_spell import MagicSpell


class SublimeCommandSpell(MagicSpell):
    required_args = ['command']

    def cast(self):
        spell_args = self.spell.get('args')

        args = spell_args.get('args') or {}
        command = spell_args.get('command')

        self.window.run_command(command, args)
