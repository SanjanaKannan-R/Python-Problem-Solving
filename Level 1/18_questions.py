'''Problem 18
Question: Get a two-digit number from user and make the ten's digit 1, then print it.
Testcase:
Input: 95 → Output: 15
Input: 82 → Output: 12'''

number = int(input())
if number >=10 and number <=99:
    ones=number%10
    result=10+ones
    print(result)