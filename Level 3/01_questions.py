'''Problem 1
Question: Get a number from user and add 2 to that number and print the result. Write
your code inside the function.
Testcase:
Input: 45 → Output: 47
Input: 56789 → Output: 56791'''


def add_two_to_number():
    num = int(input("Enter a number: "))
    result = num + 2
    print("Result:", result)
add_two_to_number()
