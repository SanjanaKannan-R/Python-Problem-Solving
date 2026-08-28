'''Problem 14
Question: Get a three-digit number from user and print the reverse of the number.
Testcase:
Input: 561 → Output: 165
Input: 859 → Output: 958'''

number = int(input())
if number >=100 and number <=999:
    hundreds = number//100
    tens=(number//10)%10
    ones=number%10
    reverse=hundreds+ones*100+tens*10
    print(reverse)