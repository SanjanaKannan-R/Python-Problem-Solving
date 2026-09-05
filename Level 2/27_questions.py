'''roblem 27
Question: Write a program to print the total count of numbers less than 100000 whose
sum of digits is 14.
Testcase:
Output: 4995'''

count = 0
for num in range(100000):
    if sum(int(digit) for digit in str(num)) == 14:
        count += 1
print(count)