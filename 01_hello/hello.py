#! /Users/tyson/.virtualenvs/tiny_python_projects/bin/python
"""
Authors: TEF, KYC
Purpose: Say Hello
"""


import argparse


def get_args():
    '''
    Add parameter and help to program
    '''
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    '''
    Main function with Jazz hands
    '''
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
