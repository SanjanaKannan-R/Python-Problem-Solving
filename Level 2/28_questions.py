'''Problem 28
Question: Write a program to get two numbers from the user and print the LCM of those
numbers.
Testcase:
Input: 12, 18 → Output: 36
Input: 15, 20 → Output: 60'''


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM of", num1, "and", num2, "is", lcm(num1, num2))