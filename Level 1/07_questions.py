'''Problem 7
Question: Get a two-digit number from user and print the ten's digit.
Testcase:
Input: 45 → Output: 4
Input: 56 → Output: 5'''

number = int(input())
if number >=100 and number <= 999:
    tens_digit = (number//10) % 10 
    print(tens_digit)