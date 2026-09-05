'''Problem 3
Question: Get a number from user and check whether the sum of digits is 14, then print
the result.
Testcase:
Input: 59 → Output: Sum of Digits is 14
Input: 123 → Output: Sum of Digits is not 14''' 


def check_sum_of_digits():
    num = int(input("Enter a number: "))
    sum_of_digits = sum(int(digit) for digit in str(num))
    if sum_of_digits == 14:
        print("Sum of Digits is 14")
    else:
        print("Sum of Digits is not 14")
check_sum_of_digits()
