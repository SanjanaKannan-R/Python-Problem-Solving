'''Problem 3
Question: Get a three-digit number from the user and print the digit in the one's position.
Testcase:
Input: 738 → Output: 8'''

def get_ones_digit():
    num = input()
    ones_digit = num[-1]
    print( ones_digit)