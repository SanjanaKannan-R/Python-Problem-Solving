'''Problem 18
Question: Write a program to get a number from the user and print whether the last two
digits form a prime number.
Testcase:
Input: 359 → Output: Prime
Input: 3577 → Output: Not Prime'''

num = int(input())
last_two_digits = num % 100

if last_two_digits > 1:
    for i in range(2, int(last_two_digits**0.5) + 1):
        if last_two_digits % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")