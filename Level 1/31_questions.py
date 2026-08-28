'''Problem 31
Question: Get a three-digit number from user. If the sum of the digits is less than 10, then print
the sum, otherwise add the digits of the sum and continue until the result is a single digit.
Testcase:
Input: 123 → Output: 6
Input: 149 → Output: 5
Input: 991 → Output: 1.'''

number=int(input())
hundreds=number//100
tens=(number//10)%10
ones=number%10
sum=hundreds+tens+ones
while sum>=10:
    sum=(sum//10)+(sum%10)
    print(sum)