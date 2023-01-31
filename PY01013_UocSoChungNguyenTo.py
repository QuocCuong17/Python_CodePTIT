import math
def snt(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n%i==0):
            return False
    return True
for t in range (int(input())):
    n,m=map(int,input().split())
    s=str(math.gcd(n,m))
    sum=0
    for i in  s:
        sum+=(int)(i)
    if(snt(sum)): print("YES")
    else:print("NO")