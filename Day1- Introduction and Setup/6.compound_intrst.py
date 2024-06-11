"""
Calculate the compound interest for a given principal
amount, interest rate, and time period

Calculate the Amount ((A)):
A=P*(1+r/n)**(n*t)

interest formula:
CI=A-P

"""
pa=float(input("Principal amount: "))
ir=float(input("Interest rate: "))
cf=int(input("Compounding frequency: "))
tp=float(input("Time period: "))

amount=pa*(1+ir/cf)**(cf*tp)

ci=amount-pa

print("Compound interest= ",ci)