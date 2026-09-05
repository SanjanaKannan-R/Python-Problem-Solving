'''Problem 4
Question: Get a three-digit number from the user and print the digit in the ten's position.
Testcase:
Input: 738 → Output: 3'''

def get_tens_digit():
    num = input()
    tens_digit = num[-2]
    print( tens_digit)
get_tens_digit()