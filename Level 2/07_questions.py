'''Problem 7
Question: Write a loop program to print the two-digit odd numbers whose sum of digits
is 7.
Testcase:
Output:
25
43
61'''

for i in range(10,100):
    if i % 2 != 0:
        digit_sum = sum(int(digit) for digit in str(i))
        if digit_sum == 7:
            print(i)