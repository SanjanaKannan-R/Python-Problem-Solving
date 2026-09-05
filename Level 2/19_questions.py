'''Problem 19
Question: Write a program to get a 4-digit number from the user and print whether the
middle two digits form a prime number.
Testcase:
Input: 6359 → Output: Not Prime
Input: 3517 → Output: Prime'''

num = int(input())
middle_two_digits = (num // 10) % 100

if middle_two_digits > 1:
    for i in range(2, int(middle_two_digits**0.5) + 1):
        if middle_two_digits % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")