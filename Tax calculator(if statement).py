#In this program it is assumed that the tax below $85528 is different than equal to or above $85528
#The tax is rounded after being calculated
#Currency name is "thalers"
income = float(input("Enter the annual income: "))
tax = float(0)

if income<85528:
    tax = 0.18 * income - 556.02
else:
    tax = 14839.02 + (0.32*( income - 85528 ))

if tax<0:
    tax = 0
tax = round(tax, 0)

print("The tax is:", tax, "thalers")
