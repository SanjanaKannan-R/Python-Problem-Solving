'''Problem 12
Question: Get a three-digit number from user and print sum the digits.
Testcase:
Input: 562 → Output: 13
Input: 469 → Output: 1'''

number = int(input())
if number >=100 and number <=999:
    hundreds = number//100
    tens=(number//10)%10
    ones=number%10
    sum=hundreds+tens+ones
    print(sum)
