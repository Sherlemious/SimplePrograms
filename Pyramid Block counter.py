blocks = int(input("Enter the number of blocks: "))
height = 1
while blocks > 0:
    blocks -= height
    if blocks < 0:
        height -= 1
    height +=1
height -= 1
print("The height of the pyramid:", height)
