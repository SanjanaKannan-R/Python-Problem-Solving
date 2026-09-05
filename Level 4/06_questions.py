'''Problem 6
Question: Get a two-digit number from the user and print its reverse.
Testcase:
Input: 73 → Output: 37'''

def print_reverse():
    num = (input())
    if len(num) == 2 and num.isdigit():
        print(num[::-1])
    else:
        print()
print_reverse()