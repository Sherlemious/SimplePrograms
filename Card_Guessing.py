##This is a program that counts cards already seen from a deck of cards and outputs whether the next card is more likely to be higher or lower than the previous one.

def up():
    print("Choose up")
def down():
    print("Choose down")

CountA=int(4)
Count2=int(4)
Count3=int(4)
Count4=int(4)
Count5=int(4)
Count6=int(4)
Count7=int(4)
Count8=int(4)
Count9=int(4)
Count10=int(4)
CountJ=int(4)
CountQ=int(4)
CountK=int(4)
value="2"
while value!="done":
    value=input("Enter card value:")
    if value == "A"or value =="a":
        CountA-=1
        if CountA>=Count2+Count3+Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountK:
            down()
        else: up()
    if value == "2":
        Count2-=1
        if Count2+Count3+Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountK>=CountA:
            up()
        else: down()
    if value == "3":
        Count3-=1
        if Count3+Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountK>=Count2+CountA:
            up()
        else: down()
    if value == "4":
        Count4-=1
        if Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountK>=Count2+Count3+CountA:
            up()
        else: down()
    if value == "5":
        Count5-=1
        if Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountK>=Count2+Count3+Count4+CountA:
            up()
        else: down()
    if value == "6":
        Count6-=1
        if Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountK>=Count2+Count3+Count4+Count5+CountA:
            up()
        else: down()
    if value == "7":
        Count7-=1
        if Count7+Count8+Count9+Count10+CountJ+CountQ+CountK>=Count2+Count3+Count4+Count5+Count6+CountA:
            up()
        else: down()
    if value == "8":
        Count8-=1
        if Count8+Count9+Count10+CountJ+CountQ+CountK>=Count2+Count3+Count4+Count5+Count6+Count7+CountA:
            up()
        else: down()
    if value == "9":
        Count9-=1
        if Count9+Count10+CountJ+CountQ+CountK>=Count2+Count3+Count4+Count5+Count6+Count7+Count8+CountA:
            up()
        else: down()
    if value == "10":
        Count10-=1
        if Count10+CountJ+CountQ+CountK>=Count2+Count3+Count4+Count5+Count6+Count7+Count8+Count9+CountA:
            up()
        else: down()
    if value == "J"or value =="j":
        CountJ-=1
        if CountJ+CountQ+CountK>=Count2+Count3+Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountA:
            up()
        else: down()
    if value == "Q"or value =="q":
        CountQ-=1
        if CountQ+CountK>=Count2+Count3+Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountA:
            up()
        else: down()
    if value == "K"or value =="k":
        CountK-=1
        if CountK>=Count2+Count3+Count4+Count5+Count6+Count7+Count8+Count9+Count10+CountJ+CountQ+CountA:
            up()
        else: down()
