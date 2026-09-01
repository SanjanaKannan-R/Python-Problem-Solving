'''Problem 34
Question: Get two 3-digit numbers from user. Print the difference between the one's digit and
hundred's digit of the number whose ten's digit is bigger than the other number's ten's digit.
Testcase:
Input: 856, 978 → Output: 1
Input: 128, 365 → Output: 2'''

number1=int(input())
number2=int(input())
if number1 // 10 % 10 > number2 // 10 % 10:
    print(number1 % 10 - number1 // 100)
else:
    print(number2 % 10 - number2 // 100)

            
