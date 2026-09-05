'''Problem 8
Question: Get a number from user and check whether its digits are in ascending order.
Testcase:
Input: 1234 → Output: Yes
Input: 5687 → Output: No'''


def check_ascending_order():
    num = input("Enter a number: ")
    if all(num[i] <= num[i + 1] for i in range(len(num) - 1)):
        print("Yes")
    else:
        print("No")
check_ascending_order()
