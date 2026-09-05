'''Problem 30
Question: Write a program to get two numbers from the user and print the HCF of those
numbers.
Testcase:
Input: 12, 18 → Output: 6
Input: 24, 36 → Output: 12'''


def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    while True:
        if x % smaller == 0 and y % smaller == 0:
            hcf = smaller
            break
        smaller -= 1
    return hcf
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("HCF of", num1, "and", num2, "is", hcf(num1, num2))