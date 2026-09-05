'''Problem 25
Question: Write a program to get a number from the user and print the total number of
single-digit prime numbers in the number.
Testcase:
Input: 163496481 → Output: 1
Input: 364925 → Output: 3'''

num = int(input())
count = 0
while num > 0:
    digit = num % 10
    if digit in [2, 3, 5, 7]:
        count += 1
    num //= 10
print(count)