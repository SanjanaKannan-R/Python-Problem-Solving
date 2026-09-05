'''Problem 6
Question: Get a number from user and reverse that number.
Testcase:
Input: 123 → Output: 321
Input: 56789 → Output: 98765'''


def reverse_number():
    num = input("Enter a number: ")
    reversed_num = num[::-1]
    print("Reversed number:", reversed_num)
reverse_number()
