''' Problem 11
Question: Get a two-digit number from user and print sum the digits.
Testcase:
Input: 56 → Output: 11
Input: 69 → Output: 15.'''

number = int(input())
if number >=10 and number <=99:
    tens=number//10
    ones=number%10
    sum=tens+ones
    print(sum)