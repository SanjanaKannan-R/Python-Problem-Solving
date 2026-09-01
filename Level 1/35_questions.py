'''Problem 35
Question: Get two 3-digit numbers from user. Add the one's and hundred's digits of both
numbers. Print the sum of all the digits of the number whose sum of one's and hundred's digits
is bigger.
Testcase:
Input: 856, 978 → Output: 24
Input: 128, 365 → Output: 11'''

number1=int(input())
number2=int(input())
sum1 = number1 % 10 + number1 // 100
sum2 = number2 % 10 + number2 // 100
if sum1 > sum2:
    biggest = number1
else:
    biggest = number2
sum_of_digits = 0
while biggest > 0:
    sum_of_digits += biggest % 10
    biggest //= 10
print(sum_of_digits)
