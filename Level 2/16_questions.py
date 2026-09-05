'''Problem 16
Question: Write a program to get a number from the user and print whether that number
is prime or not.
Testcase:
Input: 31 → Output: Prime
Input: 27 → Output: Not Prime'''

num = int(input())
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
        