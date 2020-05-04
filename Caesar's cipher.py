def prompt():
    global shift
    while True:
        shift=int(input("Please enter the shift value\n"))
        if shift>=1 and shift<=25:
            break

def crypt():
    global text, shift, new
    new=str()
    text=input("Enter the text you want to encrypt\n")
    prompt()
    for ch in text:
        if ord(ch)<=(90-shift) and ord(ch)>=65:
            new = new + (chr(ord(ch)+shift))
        elif ord(ch)>(90-shift) and ord(ch)<=90:
            new = new + (chr(ord(ch)-26+shift))
        elif ord(ch)<=(122-shift) and ord(ch)>=97:
            new = new + chr(ord(ch)+shift)
        elif ord(ch)>(122-shift) and ord(ch)<=122:
            new = new + (chr(ord(ch)-26+shift))
        else:new = new + ch
    print(new)
crypt()
