'''Problem 10
Question: Get a three-digit number from the user and print the sum of all digits.
Testcase:
Input: 738 → Output: 18'''

def sum_of_digits():
    num = input()
    if len(num) == 3 and num.isdigit():
        total = sum(int(digit) for digit in num)
        print(total)
    else:
        print()
sum_of_digits()