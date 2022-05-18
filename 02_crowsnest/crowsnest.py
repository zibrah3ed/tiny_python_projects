#!/usr/bin/env python3
"""
Author : Tyson Funk <zibrah3ed@gmail.com>
Date   : 2021-06-23
Purpose: Ahoy Narwhol
"""

import argparse
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crowsnest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        type=str,
                        help='A word',
                        )

    parser.add_argument('-s',
                        '--side',
                        metavar='side',
                        type=str,
                        default='larboard',
                        help='Pick a side default larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side
    template = 'Ahoy, Captain, {} {} off the {} bow!'
    error_template = "Try again dumbass {} isn't a word"

    char = word[0].lower()
    article = ''
    if char in 'aeiou':
        article = 'an'
    else:
        article = 'a'

    article = article.capitalize() if word[0].isupper() else article

    sentence = template.format(article, word, side)

    if char.isdigit() or string.punctuation.count(char)>0:
        print(error_template.format(word))
    else:
        print(sentence)


# --------------------------------------------------
if __name__ == '__main__':
    main()
