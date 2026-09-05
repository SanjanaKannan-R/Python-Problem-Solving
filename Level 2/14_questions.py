'''Problem 14
Question: Write a program to get a number from the user and interchange the first and
last digits, then print the result.
Testcase:
Input: 123456 → Output: 623451
Input: 76895439 → Output: 96895437
Input: 675 → Output: 576'''

num = int(input())
num_str = str(num)
if len(num_str) > 1:
    num_str = num_str[-1] + num_str[1:-1] + num_str[0]
print(int(num_str))