import unittest
import typograf as t


# TODO добавить проверку не ломающихся тегов
class TestTypograf(unittest.TestCase):
    def test_convert_quotes(self):
        self.assertEqual(
            t.convert_quotes('замена кавычек \' и \" \'раз\' \"два\"'),
            'замена кавычек \' и \" «раз» «два»'
        )

    def test_convert_hyphen_to_dash(self):
        self.assertEqual(
            t.convert_hyphen_to_dash('раз-два раз - два'),
            'раз-два раз \u2013 два'
        )

    def test_fix_dashes_in_phones(self):
        self.assertEqual(
            t.fix_dashes_in_phones('+7(999)999\u201399\u201399'),
            'раз-два раз \u2013 два'
        )

    def test_put_non_breaking_space_after_numbers(self):
        self.assertEqual(
            t.put_non_breaking_space_after_numbers('10 000 руб.'),
            '10\u00A0000\u00A0руб.'
        )

    def test_remove_extra_space(self):
        self.assertEqual(
            t.remove_extra_space('раз    два\n\r\n\n\r\rтри'),
            'раз два\nтри'
        )

    def test_link_conjunctions_with_words(self):
        self.assertEqual(
            t.link_conjunctions_with_words('кофе с молоком'),
            'кофе\u00A0с\u00A0молоком'
        )


if __name__ == '__main__':
    unittest.main()
