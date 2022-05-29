import string
import sys
import re
import itertools as it
ALPHA = string.ascii_uppercase

def load_words():
    with open('words.txt') as f:
        all_words = f.read().strip()
    return all_words

def read_cols(in_file):
    with open(in_file) as f:
        cols = [line.strip() for line in f]
        cols, known = cols[:-1],cols[-1]
        if not known: known = ALPHA
    return cols, known

def get_let(cols=None, known=None):
    if cols:
        word_dic = dict(zip(range(1,6),cols))

    if cols==None:
        print('---ORANGE LETTERS---')
        col1 = input('First col lets:\n')
        col2 = input('Second col lets:\n')
        col3 = input('Third col lets:\n')
        col4 = input('Fourth col lets:\n')
        col5 = input('Fifth col lets:\n')

        word_dic = dict(zip(range(1,6),(col1,col2,col3,col4,col5)))

        print('---AVAILABLE LETTERS---')
        known = input('All possible lets:\n').upper()
        if not known: known = ALPHA

    return word_dic, known

def main(f):
    if f:
        cols, known = read_cols(f[0])
    else: cols,known = None, None

    word_dic, known = get_let(cols, known)
    in_word = ''.join(set(''.join([str(item) for item in
                                word_dic.values()]))).upper()
    known_set = set(known)
    opts = []
    for i in range(1,6):
        if word_dic[i].isupper():
            opts.append(word_dic[i])
        else:
            opts.append(''.join(known_set - set(word_dic[i])).upper())

    opts = [''.join(opt) for opt in it.product(*opts)]
    all_words = load_words()
    valid_opts = [opt for opt in opts if opt in all_words]
    valid_opts = [opt for opt in valid_opts if all(c in opt for c in in_word)]
    [print(opt,end='\n')for opt in valid_opts]


if __name__=='__main__':
    main(sys.argv[1:])

