'''Problem 1
Question: Get a two-digit number from the user and print the digit in the one's position.
Testcase:
Input: 78 → Output: 8'''

def get_ones_digit():
    num = input()
    ones_digit = num[-1]
    print( ones_digit)
get_ones_digit()