'''Problem 7
Question: Get two numbers from user and compare them. If they are the same, print
Same; otherwise print Not Same.
Testcase:
Input: 123, 123 → Output: Same
Input: 56789, 12345 → Output: Not Same'''


def compare_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 == num2:
        print("Same")
    else:
        print("Not Same")
compare_numbers()
