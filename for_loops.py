"""
title: for_loops
author: Fariah Mahmood
date: 7/19/18 11:08 AM
"""


def fill_ticket():
    guess_list = []
    for snickers in range(5):
        num = int(input("Please enter a number: "))
        guess_list.append(num)
    return guess_list


def find_matches(secret, guesses):
    num_matches = 0
    for yes in range(5):
        if secret[yes] == guesses[yes]:
            num_matches += 1
    return num_matches


def create_string():
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
    output = ''
    for letter in letters:
        output += letter
    return output


def short_hand(phrase):
    phrase = phrase.replace('for', '4')
    phrase = phrase.replace('too', '2')
    phrase = phrase.replace('and', '&')
    phrase = phrase.replace('you', '5829')
    phrase = phrase.replace('You', '5829')

    removing = 'aeiouAEIO'
    for letter in removing:
        phrase = phrase.replace(letter, '')
    phrase = phrase.replace('5829', 'U')

    print(phrase)

if __name__ == '__main__':
    guesses = fill_ticket()
    print(guesses)
    print(create_string())
    secret = [1, 2, 3, 4, 5]
    print(find_matches(secret, guesses))
    # print(short_hand('Thank you for that! You are too sweet and kind!'))
