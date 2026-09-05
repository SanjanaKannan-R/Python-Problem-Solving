'''Problem 9
Question: Write a loop program to print the sum of two-digit numbers whose one's digit
is 5.
Testcase:
Output: 495'''

sum_of_numbers = 0
for i in range(10, 100):
    if i % 10 == 5:
        sum_of_numbers += i
print(sum_of_numbers)