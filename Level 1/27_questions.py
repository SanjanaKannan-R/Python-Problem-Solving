'''Problem 27
Question: Get a three-digit number from user. If the sum of the digits is 10 then print "Success",
otherwise print "Failure".
Testcase:
Input: 956 → Output: Failure
Input: 127 → Output: Success'''

number=int(input())
hundreds=number//100
tens=(number//10)%10
ones=number%10
sum=hundreds+tens+ones
if(sum==10):
    print("Success")
else:
    print("Failure")
