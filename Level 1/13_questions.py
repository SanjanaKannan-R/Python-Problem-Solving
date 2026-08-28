'''Problem 13
Question: Get a two-digit number from user and print the reverse of the number.
Testcase:
Input: 56 → Output: 65
Input: 59 → Output: 95'''

number = int(input())
if number >= 10 and number <=99:
    tens = number//10
    ones = number%10
    reverse= ones*10+tens
    print(reverse)