'''Problem 23
Question: Get a two-digit number from user and subtract 5 from that number if the sum of the
digits of the number is odd, then print the result. Do not use "if".
Testcase:
Input: 95 → Output: 95
Input: 72 → Output: 67.'''

number=int(input())
tens=number//10
ones=number%10
sum=tens+ones
result=number-(sum%2)*5
print(result)