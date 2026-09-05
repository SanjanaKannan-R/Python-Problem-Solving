'''Problem 17
Question: Write a program to get a number from the user, print whether that number is
prime, and check whether the sum of its digits is equal to 14.
Testcase:
Input: 59 → Output: Prime & Sum of Digits is 14
Input: 77 → Output: Not Prime but sum of digits is 14
Input: 13 → Output: Prime, but sum of Digits is not 14'''


num = int(input())
num_str = str(num)
sum_of_digits = sum(int(digit) for digit in num_str)
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    else:
        is_prime = True
else:
    is_prime = False
if is_prime and sum_of_digits == 14:
    print("Prime & Sum of Digits is 14")
elif not is_prime and sum_of_digits == 14:
    print("Not Prime but sum of digits is 14")
elif is_prime and sum_of_digits != 14:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime and sum of Digits is not 14")