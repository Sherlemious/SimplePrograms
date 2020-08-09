prev1=1
prev2=2
new=0
teven=2
while new<=4000000:
    new=prev1+prev2
    prev1=prev2
    prev2=new
    if new%2==0: teven+=new
print(teven)
