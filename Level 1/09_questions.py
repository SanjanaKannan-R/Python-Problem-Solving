'''Problem 9
Question: Get a three-digit number from user and print the hundred's digit.
Testcase:
Input: 456 → Output: 4
Input: 569 → Output: 5.'''

number = int(input())
if number >=100 and number <=999:
    digit = number//100
    print(digit)