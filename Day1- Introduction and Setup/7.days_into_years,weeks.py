"""
Write a program that converts a given number of days
into years, weeks, and days
"""
day=int(input("Give number of days: "))

year=day/365
print(f"{day} days into years are {year}")

week=day/7
print(f"{day} days into weeks are {week}")