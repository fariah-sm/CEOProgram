"""
title: branching
author: Fariah Mahmood
date: 7/18/18 11:53 AM
"""
import math
import random

def food_order(choice, menu):
    if choice in menu:
        return f"Your choice {choice} is on the menu. It will be ready soon."
    else:
        return 'We do not have the dish.'


def guess_number(low, high):
    """Tell user if guess out of range"""
    guess = input(f"Give a number between {low} and {high}")
    guess = int(guess)
    if guess < low:
        return f"No, {guess} is less than {low}"
    elif guess > high:
        return f"No, {guess} is greater than {high}"
    else:
        comp_guess = math.floor(random.randint(low, high))
        print(comp_guess)
        if comp_guess != guess:
            return "Nah. Not correct homie."
        else:
            return "GOOD JOB!!!"


if __name__ == '__main__':
    # menu = ['pizza', 'salad', 'sushi', 'fajitas', 'omelettes']
    # choice = input("Enter your choice of entree: ")
    # print(food_order(choice, menu))
    print(guess_number(1, 80))
