'''Problem 2
Question: Get a two-digit number from the user and print the digit in the ten's position.
Testcase:
Input: 78 → Output: 7'''

def get_tens_digit():
    num = input()
    tens_digit = num[-2]
    print( tens_digit)
get_tens_digit()