"""
Implement a program that swaps the values of two
variables.
"""
a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))

print(f"SWAPPING {a} 🔁 {b}")
temp=a
a=b
b=temp

print("After SWAPPING")

print("Value of a: ",a)
print("Value of b: ",b)