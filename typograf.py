from re import sub


def convert_quotes(text):
    text = sub(r'\'([^"«»]*)\'', r'«\1»', text)
    return sub(r'"([^\'«»]*)"', r'«\1»', text)


def convert_hyphen_to_dash(text):
    return sub(r'\s-\s', ' \u2013 ', text)


def fix_dashes_in_phones(text):
    return sub(
        r'((?:(?:\+7)|(?:8))\s?\(?\d{3}\)?\s?\d{3})(?:\s?[-\s\u2013]\s?)(\d{2})(?:\s?[-\s\u2013]\s?)(\d{2})',
        r'\1-\2-\3',
        text
    )


def put_non_breaking_space_after_numbers(text):
    return sub(r'(\d+)(?:\s+)', r'\1' + '\u00A0', text)


def remove_extra_space(text):
    text = sub(r'[\t\f\v ]+', ' ', text)
    return sub(r'[\r\n]+', '\n', text)


def link_conjunctions_with_words(text):
    return sub(r'(?:\s+([\wА-Яа-я]{1,2})\s+)', '\u00A0' + r'\1' + '\u00A0', text)


if __name__ == '__main__':
    print(convert_quotes('замена кавычек \' и \" \'раз\' \"два\"'))
    print(convert_hyphen_to_dash('раз-два раз - два'))
    print(fix_dashes_in_phones('текст +7(999)999\u201399\u201399 текст'))
    print(put_non_breaking_space_after_numbers('10 000 руб.'))
