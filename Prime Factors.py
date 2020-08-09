flag=True
primelist=[]
n = int(input())
end = n
fac = 1
def checkdivisible(toc):
    global primelist, n, fac
    if n%toc==0:
        primelist.append(toc)
        n=n/toc
        fac*=toc
for i in range (2,end):
        checkdivisible(i)
        if fac==end:
            break
print(primelist)
