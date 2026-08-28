'''Problem 26
Question: Get a two-digit number from user. If the sum of the digits is 10 then print "Success",
otherwise print "Failure".
Testcase:
Input: 56 → Output: Failure
Input: 37 → Output: Success'''

number = int(input())
tens=number//10
ones=number%10
if tens+ones==10:
    print("Success")
else:
    print("Failure")