'''Problem 9
Question: Get a two-digit number from the user and print the sum of all digits.
Testcase:
Input: 78 → Output: 15'''

def sum_of_digits():
    num = input()
    if len(num) == 2 and num.isdigit():
        digit_sum = sum(int(digit) for digit in num)
        print("Sum of digits:", digit_sum)
    else:
        print()
sum_of_digits()
