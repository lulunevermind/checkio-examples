import re
from io import StringIO
import sys

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    def make_cow(text):
        stream = StringIO()
        sys.stdout = stream

        top = ' ' + '_' * (max_chunks_len + 2)
        text_start = '/ {:<' + str(max_chunks_len) + '} \\'
        middle_simple = '< {:<' + str(max_chunks_len) + '} >'
        middle_long = '| {:<' + str(max_chunks_len) + '} |'
        text_end = '\ {:<' + str(max_chunks_len) + '} /'
        bot = ' ' + '-' * (max_chunks_len + 2) + COW

        print(top)
        if len(text) == 1:
            print(middle_simple.format(text[0]))
        if len(text) == 2:
            print(text_start.format(text[0]))
            print(text_end.format(text[1]))
        if len(text) > 2:
            for i, el in enumerate(text):
                if i == 0:
                    print(text_start.format(el))
                if i == (len(text) - 1):
                    print(text_end.format(el))
                if 0 < i < (len(text) - 1):
                    print(middle_long.format(el))
        print(bot)
        return stream

    max_chunks_len = 39
    stripped = re.sub('\s+', ' ', text)
    if len(text) < max_chunks_len:
        max_chunks_len = len(text)
        stream = make_cow([stripped])
    else:
        chunks = make_chunks_true(text, max_chunks_len)
        stream = make_cow(chunks)
    return '\n' + stream.getvalue()[:-1]


def make_chunks_true(text, max_len):
    chunks = []
    chunk = ""
    for w in text.split():
        if len(w) + len(chunk) > max_len:
            chunk = chunk[:-1]
            chunks.append(chunk)
            chunk = w + ' '
        else:
            chunk += w + ' '
    chunk = chunk[:-1]
    chunks.append(chunk)
    return chunks

if __name__ == '__main__':
    # print(make_chunks_true('FIRSTWORD1111111111111111 SECONDWORD THIRDWORD333333333333333   FORTHWORD4444444444444444  FIFHWORD55555555555555555555'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    # mycow = cowsay('Checkio rulezz')
    mycow = cowsay('A longtextwithonlyonespacetofittwolines.')
    # mycow = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
    #                            'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    sys.stdout = sys.__stdout__
    print(mycow)
    print(expected_cowsay_two_lines)
    # cowsay_one_line = cowsay('Checkio rulezz')
    # assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line
    #
    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines
    #
    # cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
    #                            'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    # assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
