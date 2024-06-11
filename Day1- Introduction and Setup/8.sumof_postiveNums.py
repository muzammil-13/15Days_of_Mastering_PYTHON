"""
Given a list of integers, find the sum of all positive
numbers
"""
integers = [1, 2, 3, 4, -4, -3, -2, -1]

p_sum = 0

for i in integers:
    if i >= 0:
        p_sum += i
    else:
        pass

print("sum of positive numbers= ", p_sum)
