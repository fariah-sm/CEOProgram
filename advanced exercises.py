"""
title: advanced exercises
author: Fariah Mahmood
date: 7/19/18 10:07 AM
"""


# tuples

def finding_vowels():
    yes = input("Please enter a word or keysmash.")
    vowel = set('aeiouAEIOU')
    if vowel.intersection(yes):
        return True
    else:
        return False


if __name__ == '__main__':
    print(finding_vowels())


def birthday_month(current, birthday):
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
              'September': 9, 'October': 10, 'November': 11, 'December': 12}
