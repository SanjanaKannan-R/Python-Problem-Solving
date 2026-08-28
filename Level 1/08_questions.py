'''Problem 8
Question: Get a three-digit number from user and print the one's digit.
Testcase:
Input: 456 → Output: 6
Input: 569 → Output: 9'''

number = int(input())
if number >=100 and number <=999:
    ones_digit = number%10
    print(ones_digit)