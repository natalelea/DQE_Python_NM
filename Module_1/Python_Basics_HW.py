# Function from the following library is necessary for generating random numbers
import random

# Create empty or equal to 0 variables to store the further results
numbers_list = []
sum_odd = 0
sum_even = 0
count_odd = 0
count_even = 0

# Determine quantity of random numbers to put into the list
n = 100

# Populate the created list with n random numbers from 0 to 1000
for i in range(n):
    numbers_list.append(random.randint(0, 1000))

# List will be sorted by Bubble method
for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):

        # Compare the current element with the one after it
        if numbers_list[i] > numbers_list[j]:

            # Values are swapped if two of them are not from min to max
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]

# Calculate sum and count of even numbers and odd numbers depending on remainder from division by 2
for i in numbers_list:
    if i % 2 == 1:
        sum_odd += i
        count_odd += 1
    elif i % 2 == 0:
        sum_even += i
        count_even += 1

# Calculate average for even numbers and odd numbers using zero division exception handling
try:
    avg_odd = sum_odd / count_odd
except ZeroDivisionError:
    avg_odd = 'Undefined'
    print("Division by 0. Operation can't be executed for odd numbers")

try:
    avg_even = sum_even / count_even
except ZeroDivisionError:
    avg_even = 'Undefined'
    print("Division by 0. Operation can't be executed for even numbers")

print(f"Average for odd numbers is {avg_odd} \nAverage for even numbers is {avg_even}")