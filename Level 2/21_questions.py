'''Problem 21
Question: Write a program to get a number from the user and print the total number of
digits that are odd.
Testcase:
Input: 12345678 → Output: 4
Input: 987531 → Output: 5'''

num = int(input())
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        count += 1
    num //= 10
print(count)