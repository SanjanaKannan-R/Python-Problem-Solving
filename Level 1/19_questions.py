'''Problem 19
Question: Get a three-digit number from user and make the one's digit as 2, then print it.
Testcase:
Input: 695 → Output: 692
Input: 182 → Output: 182'''

number = int(input())
if number >=100 and number <=999:
    hundreds = number//100
    tens= (number//10)%10
    ones=number%10
    new=hundreds*100+tens*10+2
    print(new)