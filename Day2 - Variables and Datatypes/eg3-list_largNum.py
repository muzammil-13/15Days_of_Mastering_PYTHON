"""
Implement a program that finds the largest number
 in a list.
"""
numbers=[1341,234,325,4,22,343,5,4,34000]
print("Number list: ",numbers)
larg=numbers[0]

for i in numbers:
    if i > larg:
        larg=i

print("Largest number in the list: ",larg)