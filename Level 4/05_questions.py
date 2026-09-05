'''Problem 5
Question: Get a three-digit number from the user and print the digit in the hundred's
position.
Testcase:
Input: 738 → Output: 7'''

def get_hundreds_digit():
    num = input()
    hundreds_digit = num[-3]
    print( hundreds_digit)  