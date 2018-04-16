import unittest
import typograf as t


class TestTypograf(unittest.TestCase):
    def test_convert_quotes(self):
        self.assertEqual(
            t.convert_quotes('замена кавычек <span class=\'quotes\'>\'кавычки\'</span> \'раз\' \"два\"'),
            'замена кавычек <span class=\'quotes\'>«кавычки»</span> «раз» «два»'
        )

    def test_convert_hyphen_to_dash(self):
        self.assertEqual(
            t.convert_hyphen_to_dash('раз-два раз - два'),
            'раз-два раз \u2013 два'
        )

    def test_fix_dashes_in_phones(self):
        self.assertEqual(
            t.fix_dashes_in_phones('текст +7(999)999\u201399-99 текст'),
            'текст +7(999)999\u201199\u201199 текст'
        )

    def test_put_non_breaking_space_after_numbers(self):
        self.assertEqual(
            t.put_non_breaking_space_after_numbers(
                '+7(999)999-99-99 <img src=\'placehold.it/60\' width=60 height=60> 10 000 руб.'
            ),
            '+7(999)999-99-99 <img src=\'placehold.it/60\' width=60 height=60> 10\u00A0000\u00A0руб.'
        )

    def test_remove_extra_space(self):
        self.assertEqual(
            t.remove_extra_space('раз    два\n\r\n\n\r\rтри'),
            'раз два\nтри'
        )

    def test_link_conjunctions_with_words(self):
        self.assertEqual(
            t.link_conjunctions_with_words('кофе с молоком'),
            'кофе с\u00A0молоком'
        )

    def test_text_general(self):
        self.assertEqual(
            t.perform(
                "замена <span class='quotes'>кавычек \'раз\' \"два\"</span> \'раз\' \"два\"\n"
                "раз-два раз - два\n"
                "текст +7(999)999\u201399-99 текст\n"
                "+7(999)999\u201399-99 10 000 руб.\n"
                "раз    два\n\r\n\n\r\rтри\n"
                "кофе с молоком"
            ),
            "замена <span class='quotes'>кавычек «раз» «два»</span> «раз» «два»\n"
            "раз-два раз \u2013 два\n"
            "текст +7(999)999\u201199\u201199 текст\n"
            "+7(999)999‑99‑99 10\u00A0000\u00A0руб.\n"
            "раз два\nтри\n"
            "кофе с\u00A0молоком"
        )


if __name__ == '__main__':
    unittest.main()
