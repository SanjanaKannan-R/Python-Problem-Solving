'''Problem 22
Question: Write a program to get a number from the user and print the total number of
two-digit odd numbers in the number.
Testcase:
Input: 12345678 → Output: 3
Input: 987531 → Output: 4'''


num = int(input())
count = 0
while num > 0:
    last_two_digits = num % 100
    if last_two_digits % 2 != 0:
        count += 1
    num //= 10
print(count)