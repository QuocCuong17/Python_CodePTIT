import math
def snt(n):
    if(n<2): return False
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0): return False
    return True
"""n,m= [int(x) for x in input().split()]"""
n,m = map(int,input().split())
for i in range(0,n):
    list=input().split()
    for x in list:
        if(snt((int)(x))): print("1",end=" ")
        else:print("0",end=" ")
    print()