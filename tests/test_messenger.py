import sublime
import sys

from base import SublimeMagicTestCase

messenger_module = sys.modules['SublimeMagic.messenger.messenger']


class TestMessenger(SublimeMagicTestCase):

    def test_message(self):
        messenger = messenger_module.Messenger()
        messenger.message(self.view, 'foo bar', False)
        self.assertEqual(self.view.get_status('SublimeMagic'), 'foo bar')

        messenger.message(self.view, 'foo bar', True)
        self.assertEqual(self.view.get_status('SublimeMagic'), 'foo bar\n')
