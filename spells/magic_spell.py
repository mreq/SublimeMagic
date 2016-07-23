class MagicSpell(object):
    required_args = []

    def __init__(self, spell):
        self.spell = spell
        self.validate_args()

    def validate_args(self):
        args = self.spell.get('args')
        for arg in self.required_args:
            if not args.get(arg, None):
                raise AttributeError('Missing arg: ' + arg)
