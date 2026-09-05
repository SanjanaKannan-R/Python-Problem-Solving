'''Problem 24
Question: Write a program to get a number from the user and print the total number of
two-digit perfect square numbers in the number.
Testcase:
Input: 163496481 → Output: 4
Input: 364925 → Output: 4'''


num = int(input())
count = 0
while num > 0:
    last_two_digits = num % 100
    if last_two_digits in [16, 25, 36, 49, 64, 81]:
        count += 1
    num //= 10
print(count)