import sublime
import sys

from base import SublimeMagicTestCase

if sublime.version() < '3000':
    context_checker_module = sys.modules['context.context_checker']
else:
    context_checker_module = sys.modules[
        'SublimeMagic.context.context_checker']


class TestContextChecker(SublimeMagicTestCase):

    def test_scope_name(self):
        checker = context_checker_module.ContextChecker(self.view)
        self.assertEqual(checker.scope_name, 'text.plain ')

    def test_line_text(self):
        self.setText('foo bar')
        checker = context_checker_module.ContextChecker(self.view)
        self.assertEqual(checker.line_text, 'foo bar')

    def test_check_scope(self):
        checker = context_checker_module.ContextChecker(self.view)

        target_scopes = ['plain']
        self.assertTrue(checker.check_scope(target_scopes))

        target_scopes = ['foobar']
        self.assertFalse(checker.check_scope(target_scopes))

    def test_check_line_matches(self):
        self.setText('foo bar')
        checker = context_checker_module.ContextChecker(self.view)

        target_parts = ['foo', 'bar', 'foo bar']
        self.assertTrue(checker.check_line_matches(target_parts))

        target_parts = ['foobar']
        self.assertFalse(checker.check_line_matches(target_parts))
