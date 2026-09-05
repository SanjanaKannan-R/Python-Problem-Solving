'''Problem 9
Question: Get a two-digit number from user and swap the digits.
Testcase:
Input: 34 → Output: 43
Input: 56 → Output: 65'''


def swap_digits():
    num = input("Enter a two-digit number: ")
    if len(num) == 2:
        swapped_num = num[::-1]
        print("Swapped number:", swapped_num)
    else:
        print("Please enter a valid two-digit number.")
swap_digits()
