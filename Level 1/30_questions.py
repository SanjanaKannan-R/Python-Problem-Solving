'''Problem 30
Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is
equal to 10, and one of the digits is more than 7 then print "Success", otherwise print "Failure".
Testcase:
Input: 4649 → Output: Failure
Input: 9286 → Output: Success.'''

number=int(input())
thousands=number//1000
hundreds=number//100%10
tens=number//10%10
ones=number%10
sum=hundreds+tens
if(sum==10 and hundreds>7 or tens>7):
    print("Success")
else:
    print("Failure")