def isPrime(num):
    flag=True
    for f in range(2,num):
        if num %(f)==0:
            flag=False
            break
    return flag
