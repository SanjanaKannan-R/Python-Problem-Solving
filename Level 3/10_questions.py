'''Problem 10
Question: Get a number from user, find the number of digits, and print it.
Testcase:
Input: 34678 → Output: 5
Input: 12345678 → Output: 8'''


def count_digits():
    num = input("Enter a number: ")
    digit_count = len(num)
    print("Number of digits:", digit_count)
count_digits()
