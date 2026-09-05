'''Problem 15
Question: Write a program to get a number from the user. If the first digit is even, print
the same number. If the first digit is odd, subtract 1 from the first digit and print the
number.
Testcase:
Input: 123456 → Output: 023456
Input: 96895439 → Output: 86895439
Input: 675 → Output: 675
Input: 575 → Output: 475'''

num = int(input())
num_str = str(num)
if int(num_str[0]) % 2 != 0:
    num_str = str(int(num_str[0]) - 1) + num_str[1:]
print(num_str)