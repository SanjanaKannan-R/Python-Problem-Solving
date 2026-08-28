'''Problem 28
Question: Get a three-digit number from user. If the sum of the one's digit and hundred's digit is
less than 10, then print "Success", otherwise print "Failure".
Testcase:
Input: 569 → Output: Failure
Input: 316 → Output: Success'''

number=int(input())
hundreds=number//100
tens=(number//10)%10
ones=number%10
sum=hundreds+ones
if (sum<10):
    print("Success")
else:
    print("Failure")