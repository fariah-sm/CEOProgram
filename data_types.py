"""
title: data_types
author: Fariah Mahmood
date: 7/18/18 10:30 AM
"""


def add_tip(total, tip_percentage):
    # return total amount including tip
    tip = tip_percentage*total
    return total + tip


x = add_tip(30, .1)
x *= 5
print(x)


def age_calculator(current_year, birth_year):
    # Returns user's age
    age = current_year - birth_year
    return age


print(age_calculator(2018, 2003))


def mean(a, b, c):
    total = (a + b + c)
    average = total/3
    return average


print(mean(4, 7, 8))


if __name__ == "__main__":
    print(age_calculator(2018, 2003))


def distance_formula(a_one, a_two, y_one, y_two):
    a = (a_one - a_two) ** 2
    y = (y_one - y_two) ** 2
    distance = ((a + y)**.5)
    return distance


print(distance_formula(7, 5, 9, 4))


