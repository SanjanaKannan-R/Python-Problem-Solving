'''Problem 17
Question: Get a two-digit number from user and make the one's digit as 0, then print it.
Testcase:
Input: 95 → Output: 90
Input: 18 → Output: 10'''

number = int(input())
if number >= 10 and number <=99:
    tens = number//10
    result = tens*10
    print(result)