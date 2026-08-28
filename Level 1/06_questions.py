'''Problem 6
Question: Get a two-digit number from user and print the one's digit.
Testcase:
Input: 45 → Output: 5
Input: 56 → Output: 6.'''

number = int(input())
if number >= 10 and number <=99:
    ones_digit = number % 10
    print(ones_digit)