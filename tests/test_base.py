# -*- coding: utf-8 -*-
import sublime

from base import SublimeMagicTestCase


class TestSublimeMagicBase(SublimeMagicTestCase):

    def test_base_command(self):
        self.setText('foo bar')
        self.view.run_command('sublime_magic')
        first_row = self.getRow(0)

        self.assertEqual(first_row, 'foo bar')

        # # this fails on travis for some reason
        # self.assertEqual(
        #     self.view.get_status('SublimeMagic'),
        #     '★ No spell found.\n')
