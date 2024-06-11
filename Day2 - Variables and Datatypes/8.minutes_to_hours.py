"""
Implement a program that converts a given number of
minutes into hours and minutes
"""
minute=int(input("Enter the minutes: "))

hours=minute//60
minutes=minute%60

print(f"{minute} minutes into {hours} Hours & {minutes} minutes")