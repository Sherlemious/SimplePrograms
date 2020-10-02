a=1
b=2
c=0
t=2
while c<=4000000:
    c=a+b
    a=b
    b=c
    if c%2==0: 
        t+=c
print(t)
