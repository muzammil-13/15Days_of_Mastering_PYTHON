"""
 Given a list of numbers, find the sum and average
"""
num = [70, 25, 42, 21, 26]
print("List of number:", num)

sum = 0
avg = 0

for i in num:
    sum += i
    avg = sum / len(num)

print("Sum of all numbers = ", sum)
print("Average of given numbers = ", avg)
