Num1= int(input("Enter the first number:"))
Num2= int(input("Enter the second number:"))
Num3= int(input("Enter the third number:"))
if Num1>Num2:
    if Num3>Num2:
                Product= int(Num1 * Num3)
    else: Product= int(Num1 * Num2)
elif Num1>Num3:
    Product= int(Num1*Num2)
else:
    Product= int(Num2 * Num3)
print(Product)
