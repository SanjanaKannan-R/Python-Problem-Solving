'''Problem 7
Question: Get a three-digit number from the user and print its reverse.
Testcase:
Input: 738 → Output: 837'''

def print_reverse():
    num = (input())
    if len(num) == 3 and num.isdigit():
        print(num[::-1])
    else:
        print()
print_reverse()