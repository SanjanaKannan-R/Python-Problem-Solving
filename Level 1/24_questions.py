'''Problem 24
Question: Get a three-digit number from user and subtract 5 from that number if one's digit and
hundred's digit are the same, then print the result. Do not use "if".
Testcase:
Input: 595 → Output: 590
Input: 372 → Output: 372.'''

number = int(input())
hundreds = number//100
ones=number%10
result=number-((hundreds==ones)*5)
print(result)