'''Problem 15
Question: Get a four-digit number from user and only reverse the first two digits of the number,
then print the number.
Testcase:
Input: 9561 → Output: 9516
Input: 3859 → Output: 3895'''

number = int(input())
if number>=1000 and number <= 9999:
    first = number // 100
    last = number % 100
    reversed = (first % 10) * 10 + (first// 10)
    result = reversed * 100 + last
    print(result)
