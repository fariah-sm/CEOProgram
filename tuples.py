"""
title: tuples
author: Fariah Mahmood
date: 7/19/18 9:48 AM
"""


import random


def name_generator(first_list, last_list):
    return f"{random.choice(first_list)}" + " " + f"{random.choice(last_list)}"


if __name__ == '__main__':
    first_list = ["Joe", "Moe", "Bo", "LoLo", "Zo"]
    last_list = ["Smith", "Rodriguez", "Hernandez", "Doe", "Phillips"]
    print(name_generator(first_list, last_list))
