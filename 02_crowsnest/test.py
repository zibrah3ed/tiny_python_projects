#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
punk_words = ['.aviso', '3eel', '?ice']
template = 'Ahoy, Captain, {} {} off the larboard bow!'
template2 = 'Ahoy, Captain, {} {} off the {} bow!'
error_template = "Try again dumbass {} isn't a word"

# --------------------------------------------------
def test_exists():
    """exists"""
    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_sideboard():
    '''Larboard or Starboard'''
    
    out = getoutput(f'{prg} ')


def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())


def test_matchcase():
    '''Apple -> An Apple'''

    for word in vowel_words:
        out = getoutput(f'{prg} {word.capitalize()}')
        assert out.strip() == template.format('An', word.capitalize())
        

def test_starboard():
    ''' Test starboard switch is functioningh'''
    
    for word in consonant_words:
        out = getoutput(f'{prg} {word} --side starboard')
        assert out.strip() == template2.format('a', word, "starboard")

def test_larboard():
    '''Test larboard ddefault'''

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word )


def test_numpunk():

    for word in punk_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == error_template.format(word)
        