"""
title: strings
author: Fariah Mahmood
date: 7/18/18 2:41 PM
"""


def how_eligible(essay):
    """Returns how many categories are in a string"""
    categories = 0
    if "?" in essay:
        categories += 1
    else:
        categories += 0
    if '"' in essay:
        categories += 1
    else:
        categories += 0
    if "," in essay:
        categories += 1
    else:
        categories += 0
    if "!" in essay:
        categories += 1
    else:
        categories += 0
    return categories


def letter_check():
    letter = input("Enter a letter.")
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in letters:
        return True
    else:
        return False


if __name__ == '__main__':
    # print(how_eligible('This? "Yes." No, not really!'))
    # print(how_eligible('Really, not a compound sentence.'))
    print(letter_check())