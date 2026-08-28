'''Problem 20
Question: Get a three-digit number from user and make the ten's digit as 0, then print it.
Testcase:
Input: 695 → Output: 605
Input: 182 → Output: 102.'''

number = int(input())
if number >=100 and number <=999:
    hundreds=number//100
    tens=(number//10)%10
    ones=number%10
    new=hundreds*100+0*tens+ones
    print(new)
    