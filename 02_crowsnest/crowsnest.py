#!/usr/bin/env python3
"""
Author : Tyson Funk <zibrah3ed@gmail.com>
Date   : 2021-06-23
Purpose: Ahoy Narwhol
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crowsnest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    # print(f'str_arg = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')

    char = word[0].lower()
    article = ''
    if char in 'aeiou':
        article = 'an'
    else:
        article = 'a'
        
    sentence = 'Ahoy, Captain, {} {} off the larboard bow!'.format(article, word)

    print(sentence)


# --------------------------------------------------
if __name__ == '__main__':
    main()
