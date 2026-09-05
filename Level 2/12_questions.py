'''Problem 12
Question: Write a program to get a number from the user and print the sum of all digits.
Testcase:
Input: 123456 → Output: 21
Input: 76895439 → Output: 51
Input: 675 → Output: 18'''

num = int(input())
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(digit_sum)