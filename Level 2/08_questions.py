'''Problem 8
Question: Write a loop program to print the two-digit even numbers whose sum of digits
is 6.
Testcase:
Output:
24
42
60'''

for i in range(10,100):
    if i % 2 == 0:
        digit_sum = sum(int(digit) for digit in str(i))
        if digit_sum == 6:
            print(i)