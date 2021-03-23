# Oliver Keen
# Software Engineering 001
# jumble_solver.py
# 2/17/2021

# Assignment:
# Consider the game "Jumble"
# https://www.sandiegouniontribune.com/sd-jumble-daily-htmlstory.html
# Create a Python program to find the individual words in Jumble puzzles such
# that INJURE prints after entering the following: solve("JNUIER")

from PyDictionary import PyDictionary # Installation: pip install PyDictionary
from math import factorial
from random import shuffle

def solve(jumble):
    combos = []
    chars = list(jumble.upper())
    dict = PyDictionary()

    # Maximum possible unique combinations of chars
    limit = factorial(len(chars))

    while len(combos) < limit:
        # Generates random string from chars
        shuffle(chars)
        tmp = "".join(chars)

        # Appends tmp to combos list only if it is unique
        if tmp not in combos:
            combos.append(tmp)

            # Prints tmp only if it returns an English meaning
            if dict.meaning(tmp, disable_errors = True):
                print(tmp)
                break
