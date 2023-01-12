import math
def snt(n):
    for i in range(2,(int)(math.sqrt(n)+1)):
        if(n%i==0) : return false
    return n>1
t=(int)(input())
while t>0 :
    t-=1
    n=int(input())
    k=0
    for i in range(1,n):
        if(math.gcd(i,n)==1):
            k+=1
    if(snt(k)): print("YES")
    else:print("NO")