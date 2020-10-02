def isPrime(num):
    flag=True
    for f in range(2,num//2):
        if num %(f)==0:
            flag=False
            break
    return flag
