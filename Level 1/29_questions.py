'''Problem 29
Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is
greater than 10, then print "Success", otherwise print "Failure".
Testcase:
Input: 7529 → Output: Failure
Input: 9386 → Output: Success.'''

number=int(input())
thousands=number//1000
hundreds=number//100%10
tens=number//10%10
sum=number%10
if(hundreds+tens>10):
    print("Success")
else:
    print("Failure")