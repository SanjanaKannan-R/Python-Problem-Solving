'''Problem 8
Question: Get a four-digit number from the user and print its reverse.
Testcase:
Input: 7384 → Output: 4837'''

def print_reverse():
    num = (input())
    if len(num) == 4 and num.isdigit():
        print(num[::-1])
    else:
        print()
print_reverse()