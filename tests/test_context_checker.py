import sublime
import sys

from base import SublimeMagicTestCase
from SublimeMagic.context import context


def c(a):
    return {
        'context': a
    }


class TestContextChecker(SublimeMagicTestCase):

    def test_check_scope(self):
        test_context = c({'scope': ['plain']})
        self.assertTrue(context.check(self.view, test_context))

        test_context = c({'scope': ['foobar']})
        self.assertFalse(context.check(self.view, test_context))

    def test_check_line_matches(self):
        self.setText('foo bar')

        test_context = c({'line_matches': ['foo', 'bar', 'foo bar']})
        self.assertTrue(context.check(self.view, test_context))

        test_context = c({'line_matches': ['foobar']})
        self.assertFalse(context.check(self.view, test_context))

    def test_check_selection(self):
        self.setText('foo bar')

        test_context = c({'selection_matches': ['bar']})
        self.assertFalse(context.check(self.view, test_context))
        test_context = c({'selection_empty': True})
        self.assertTrue(context.check(self.view, test_context))
        test_context = c({'selection_empty': False})
        self.assertFalse(context.check(self.view, test_context))

        self.view.sel().clear()
        self.view.sel().add(sublime.Region(4, 7))

        test_context = c({'selection_matches': ['bar']})
        self.assertTrue(context.check(self.view, test_context))
        test_context = c({'selection_empty': False})
        self.assertTrue(context.check(self.view, test_context))
        test_context = c({'selection_empty': True})
        self.assertFalse(context.check(self.view, test_context))
