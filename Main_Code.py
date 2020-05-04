Flag=True
from random import randrange
#Declare Board Variables
Values={
       1:"1",
       2:"2",
       3:"3",
       4:"4",
       5:"5",
       6:"6",
       7:"7",
       8:"8",
       9:"9" }

def DisplayBoard(): #7 spaces
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",Values[1],"  |  ",Values[2],"  |  ",Values[3],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",Values[4],"  |  ",Values[5],"  |  ",Values[6],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",Values[7],"  |  ",Values[8],"  |  ",Values[9],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
def EnterMove():
    while True:    
        current=int(input("Please Enter Your move as O\n"))
        if Values[current]!="X" and Values[current]!="O":
            Values[current]="O"
            break
    else:print("This option is already taken")
        
def check(i):
    global Flag
    if Values[i]=="O" or Values[i]=="X":
        Flag=False
        if Values[i]=="O":
            print("Congrats! You have won the game")
        else: print("The computer has won the games")
    
def VictoryFor():
    global Flag
    if Values[1]==Values[2]==Values[3]: check(1) 
    if Values[4]==Values[5]==Values[6]: check(4) 
    if Values[7]==Values[8]==Values[9]: check(7) 
    if Values[1]==Values[4]==Values[7]: check(1) 
    if Values[2]==Values[5]==Values[8]: check(2)
    if Values[3]==Values[6]==Values[9]: check(3)
    if Values[1]==Values[5]==Values[9]: check(1)
    if Values[3]==Values[5]==Values[7]: check(3)
    

def RandDraw():
    while True:
           current=randrange(1,9)    
           if Values[current]!="X" and Values[current]!="O":
              Values[current]="X"
              break


def DrawMove():
    if Values[5]=="O" and Values[1]!=Values[2]!=Values[3]!=Values[4]!=Values[6]!=Values[7]!=Values[8]!=Values[9]!="X"!="O": Values[1]="X"
    if Values[5]=="O"==Values[3] and Values[1]=="X" and Values[2]!=Values[3]!=Values[4]!=Values[6]!=Values[7]!=Values[8]!=Values[9]!="X"!="O": Values[7]="X"
    if Values[5]=="O"==Values[3]==Values[4] and Values[1]=="X"==Values[7] and Values[2]!=Values[4]!=Values[6]!=Values[8]!=Values[9]!="X"!="O": Values[6]="X"
    if Values[5]=="O"==Values[3]==Values[4] and Values[1]=="X"==Values[7] and Values[2]!=Values[4]!=Values[6]!=Values[8]!=Values[9]!="X"!="O": Values[6]="X"

    #
    #
    #
    #



    else: RandDraw
        


#MainGame
Counter=0
while Flag and Counter!=10:
    VictoryFor()
    DisplayBoard()
    EnterMove()
    if Flag:
        VictoryFor()
        DrawMove()
    Counter+=2


if Flag == True:print("The game is a draw")
