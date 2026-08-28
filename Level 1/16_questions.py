'''Problem 16
Question: Get a four-digit number from user and only reverse the last two digits of the number,
then print the number.
Testcase:
Input: 9561 → Output: 5961
Input: 3859 → Output: 8359'''

number = int(input())
if number >= 1000 and number <= 9999:       
    first = number // 100
    last = number % 100
    reversed = (last % 10) * 10 + (last// 10)
    result = first * 100 + reversed
    print(result)