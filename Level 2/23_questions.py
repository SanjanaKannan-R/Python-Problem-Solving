'''Problem 23
Question: Write a program to get a number from the user and print the total number of
single-digit perfect square numbers in the number.
Testcase:
Input: 123456789 → Output: 3
Input: 987531 → Output: 2''' 


num = int(input())
count = 0
while num > 0:
    digit = num % 10
    if digit in [1, 4, 9]:
        count += 1
    num //= 10
print(count)