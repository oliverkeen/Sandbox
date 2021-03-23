# Oliver Keen
# Implementation of some learning exercises

# Exercise 1: Gets integer user input, then outputs only the negative values
# Example: 54 -22 -3 83 -56 4 26 0 returns -22 -3 -56
print("# This fixture gets integer input and outputs only the negative values.")
print("Enter integers one at a time, positive and negative (0 ends input):")

num = int(input())
numArr = []

while num != 0:
    numArr.append(num)
    num = int(input())

print("Your negative integers are:")

for i in numArr:
    if i < 0:
        print(str(i) + ' ', end = '')

print('\n')

# Exercise 2: Output 3 character inputs in reverse order
# Example: k t a
print("# This fixture gets str input and outputs characters in reverse order.")
chars = ""

while len(chars) != 5 or chars[1] != ' ' or chars[3] != ' ':
    chars = input("Enter three characters delimited with a space (a b c):\n")

    if len(chars) != 5 or chars[1] != ' ' or chars[3] != ' ':
        print("Invalid input, please try again.")
    else:
        print("Your reversed characters are:")
        print(chars[::-1])

print('\n')
