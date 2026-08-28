''' Problem 10
Question: Get a three-digit number from user and print the ten's digit.
Testcase:
Input: 456 → Output: 5
Input: 569 → Output: 6.'''

number = int(input())
if number >=100 and number <=999:
    digit = (number//10)%10
    print(digit)