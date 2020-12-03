# Code for Day 1 of Advent of Code 2020

## Challenge 1
### Before you leave, the Elves in accounting just need you to fix your expense 
### report (your puzzle input); apparently, something isn't quite adding up.

### Specifically, they need you to find the two entries that sum to 2020 and then 
### multiply those two numbers together.

## Challenge 2
### The Elves in accounting are thankful for your help; one of them even offers you a 
### starfish coin they had left over from a past vacation. They offer you a second one 
### if you can find three numbers in your expense report that meet the same criteria.

import itertools

# returns a list of imported numbers
def get_expenses():
    expenses = []
    with open('day1/data/expenses.txt','r') as expense_list:
        for expense in expense_list:
            expenses.append(int(expense))
    return expenses

# Challenge 1: compares each number in the list to another until it finds the sum of the combination to equal 2020
# when it finds the right combination, it multiplies the combination and returns the value
def compare_two():
    for a, b in itertools.combinations(get_expenses(), 2):
        if a + b == 2020:
            return a * b

# Challenge 2: compares each combination of three numbers in the list until it finds the sum of the combination
# to equal 2020. When it finds the right combination, it multiplies the combination and returns the value
def compare_three():
    for a, b, c in itertools.combinations(get_expenses(), 3):
        if a + b + c == 2020:
            return a * b * c

def main():
    print(compare_two())
    print(compare_three())

if __name__ == "__main__":
    main()