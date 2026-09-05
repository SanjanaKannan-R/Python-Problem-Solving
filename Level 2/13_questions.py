'''Problem 13
Question: Write a program to get a number from the user and print the reverse of that
number.
Testcase:
Input: 123456 → Output: 654321
Input: 76895439 → Output: 93459867
Input: 675 → Output: 576'''

num = int(input())
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)