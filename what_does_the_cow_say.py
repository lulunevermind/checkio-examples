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
        else:
            for el in text:
                print(middle_long.format(el))
        print(bot)
        return stream

    max_chunks_len = 39
    stripped = re.sub('\s+', ' ', text)
    if len(text) < max_chunks_len:
        max_chunks_len = len(text)
        stream = make_cow([stripped])
    else:
        chunks = [stripped[i:i+max_chunks_len] for i in range(0, len(stripped), max_chunks_len)]
        stream = make_cow(chunks)

    return '\n' + stream.getvalue()[:-1]


def make_chunks_true(text):
    max_chunks_len = 39
    chunks = []
    chunk = []
    for w in text.split():
        if len(chunk) > max_chunks_len:
            break
        else:
            chunk += w
    return chunks



if __name__ == '__main__':
    # mycow = cowsay('a asdaksjdhaksdjhaksjdhaksjdhaskjdhaksjdhakjsdhaksjdhakjshdaksdh')
    sys.stdout = sys.__stdout__
    print(make_chunks_true('a asdaksjdhaksdjhaksjdhaksjdhaskjdhaksjdhakjsdhaksjdhakjshdaksdh'))
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
    # print(expected_cowsay_one_line)
    # print(mycow == expected_cowsay_one_line)
    # print('!')
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
#
#     expected_cowsay_many_lines = r'''
#  _________________________________________
# / Lorem ipsum dolor sit amet, consectetur \
# | adipisicing elit, sed do eiusmod tempor |
# | incididunt ut labore et dolore magna    |
# \ aliqua.                                 /
#  -----------------------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
# '''

    # cowsay_one_line = cowsay('Checkio rulezz')
    # assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    # cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    # assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines
    #
    # cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
    #                            'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    # assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
