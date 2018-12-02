from re import sub


def convert_quotes(text):
    in_tag, double, single = 1, 2, 3

    return sub(
        r'(<(?:"[^"]*"|\'[^\']*\'|[^\'">])*>)|"([^"]*)"|\'([^\']*)\'',
        lambda entry:
        "{}".format(entry.group(in_tag)) if entry.group(in_tag) else
            "«{}»".format(entry.group(double) or (entry.group(single) or '')),
        text
    )


def convert_hyphen_to_dash(text):
    return sub(r'\s-\s', ' \u2013 ', text)


def fix_dashes_in_phones(text):
    return sub(
        r'((?:(?:\+7)|(?:8))\s?\(?\d{3}\)?\s?\d{3})'
        r'(?:\s?[-\s\u2013]\s?)(\d{2})'
        r'(?:\s?[-\s\u2013]\s?)(\d{2})',
        r'\1' + '\u2011' + r'\2' + '\u2011' + r'\3',
        text
    )


def put_non_breaking_space_after_numbers(text):
    return sub(r'(?<=[\u0020\u00a0])(\d+)([\u0020\u00a0]+)', '\\1\u00A0', text)


def remove_extra_space(text):
    text = sub(r'[\t\f\v ]+', ' ', text)
    return sub(r'[\r\n]+', '\n', text)


def link_conjunctions_with_words(text):
    return sub(r'(?:\s+([\wА-Яа-я]{1,2})\s+)', ' \\1\u00A0', text)


def perform(text):
    text = convert_quotes(text)
    text = convert_hyphen_to_dash(text)
    text = fix_dashes_in_phones(text)
    text = put_non_breaking_space_after_numbers(text)
    text = remove_extra_space(text)
    return link_conjunctions_with_words(text)


if __name__ == '__main__':
    print(
        perform(
            "замена <span class='quotes'>кавычек</span> \'раз\' \"два\"\n"
            "раз-два раз - два\n"
            "текст +7(999)999\u201399-99 текст\n"
            "+7(999)999\u201399-99 10 000 руб.\n"
            "раз    два\n\r\n\n\r\rтри\n"
            "кофе с молоком"
        )
    )
