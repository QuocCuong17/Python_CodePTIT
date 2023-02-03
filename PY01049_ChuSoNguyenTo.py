import math


def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0): return False
    return True
def check(s):
    if(not snt(len(s))): return 'NO'
    slCSNT=0
    for i in s:
        if(snt(int(i))):slCSNT+=1
    if(slCSNT<=len(s)-slCSNT):return 'NO'
    return 'YES'
for t in range(int(input())):
    n=input()
    print(check(n))
