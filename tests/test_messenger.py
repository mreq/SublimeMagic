import sublime
import sys

from base import SublimeMagicTestCase

if sublime.version() < '3000':
    messenger_module = sys.modules["messenger.messenger"]
else:
    messenger_module = sys.modules['SublimeMagic.messenger.messenger']


class TestMessenger(SublimeMagicTestCase):

    def test_message(self):
        messenger = messenger_module.Messenger()
        messenger.message(self.view, 'foo bar', False)
        self.assertEqual(self.view.get_status('SublimeMagic'), 'foo bar')

        messenger.message(self.view, 'foo bar', True)
        self.assertEqual(self.view.get_status('SublimeMagic'), 'foo bar\n')
