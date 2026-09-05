'''Problem 2
Question: Get a number from user and subtract 5 from that number and print the result.
Write your code inside the function.
Testcase:
Input: 45 → Output: 40
Input: 56789 → Output: 56784'''


def subtract_five_from_number():
    num = int(input("Enter a number: "))
    result = num - 5
    print("Result:", result)
subtract_five_from_number()
