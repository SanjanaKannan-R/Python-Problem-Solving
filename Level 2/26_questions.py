'''Problem 26
Question: Write a program to print the biggest 4-digit number which is divisible by 7 and
9.
Testcase:
Output: 9954'''


num = 9999
while num > 0:
    if num % 7 == 0 and num % 9 == 0:
        print(num)
        break
    num -= 1