'''Problem 5
Question: Get a number from user and count the number of zeros in that number.
Testcase:
Input: 100 → Output: 2
Input: 1060030 → Output: 4'''


def count_zeros():
    num = input("Enter a number: ")
    zero_count = num.count('0')
    print("Number of zeros:", zero_count)
count_zeros()
