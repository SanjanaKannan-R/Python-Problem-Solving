'''Problem 10
Question: Write a loop program to print the sum of two-digit odd numbers whose ten's
digit is 7.
Testcase:
Output: 375'''

sum_of_numbers = 0
for i in range(70, 80):
    if i % 2 != 0:
        sum_of_numbers += i 
print(sum_of_numbers)