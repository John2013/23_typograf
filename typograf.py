import re


def convert_quotes(text):
    in_tag, double, single = 1, 2, 3

    quote_finder_re = re.compile(
        r"""
        (<(?:"[^"]*"|\'[^\']*\'|[^\'">])*>)  # <tag attr="">
        |"([^"]*)"                           # ""
        |\'([^\']*)\'                        # ''
        """,
        re.X
    )
    return re.sub(
        quote_finder_re,
        lambda entry:
        "{}".format(entry.group(in_tag)) if entry.group(in_tag) else
            "«{}»".format(entry.group(double) or (entry.group(single) or '')),
        text
    )


def convert_hyphen_to_dash(text):
    return re.sub(r'\s-\s', ' \u2013 ', text)


def fix_dashes_in_phones(text):
    phone_re = re.compile(
        r"""
        (
            (?:(?:\+7)|(?:8))\s?     # +7 | 8
            \(?\d{3}\)?\s?           # (999)
            \d{3}                    # 999
        )
        (?:\s?[-\s\u2013]\s?)        # -
        (\d{2})                      # 99
        (?:\s?[-\s\u2013]\s?)        # -
        (\d{2})                      # 99
        """,
        re.X
    )
    return re.sub(
        phone_re,
        r'\1{0}\2{0}\3'.format('\u2011'),
        text
    )


def put_non_breaking_space_after_numbers(text):
    space_after_numbers_re = re.compile(
        r"""
        (?<=[\u0020\u00a0]) # space
        (\d+)               # number
        ([\u0020\u00a0]+)   # spaces
        """,
        re.X
    )
    return re.sub(space_after_numbers_re, '\\1\u00A0', text)


def remove_extra_space(text):
    text = re.sub(r'[\t\f\v ]+', ' ', text)
    return re.sub(r'[\r\n]+', '\n', text)


def link_conjunctions_with_words(text):
    return re.sub(r'(?:\s+([\wА-Яа-я]{1,2})\s+)', ' \\1\u00A0', text)


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
