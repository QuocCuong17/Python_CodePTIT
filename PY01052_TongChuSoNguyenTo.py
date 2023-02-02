import math


def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n%i==0): return False
    return True
def check(s):
    sum=0
    for i in s :
        sum+= int(i)
    if(snt(sum)): return 'YES'
    return 'NO'
for t in range (int(input())):
    s=input()
    print(check(s))