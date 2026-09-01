'''Problem 32
Question: Get two 2-digit numbers from user. If the sum of the numbers is less than 100, then
print the sum, otherwise print the difference.
Testcase:
Input: 56, 78 → Output: 22
Input: 14, 65 → Output: 79'''

number1=int(input())
number2=int(input())
if number1 + number2 < 100:
    print(number1 + number2)
else:
    print(number1 - number2)   
