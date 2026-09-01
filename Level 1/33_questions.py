'''Problem 33
Question: Get two 2-digit numbers from user. Print the sum of digits of the biggest number.
Testcase:
Input: 56, 78 → Output: 15
Input: 14, 65 → Output: 11'''

number1=int(input())
number2=int(input())            
if number1 > number2:
    biggest=number1
else:
    biggest=number2
sum_of_digits = 0
while biggest > 0:
    sum_of_digits += biggest % 10
    biggest //= 10
print(sum_of_digits)