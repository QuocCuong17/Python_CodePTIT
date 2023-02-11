import math


def stn(n):
    if len(str(n)) < 2: return False
    if n!=n[::-1]: return False
    return True
if __name__ == '__main__':
    n,m = map(int,input().split())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    max_val=10**-18
    vth,vtc=0,0
    b=[i for x in a for i in x]
    x=1
    for i in range(n):
        for j in range(m):
            if stn(str(a[i][j])) and a[i][j]>x:
                x=a[i][j]
    if x==1:
        print("NOT FOUND")
    else:print(x)
    for i in range(n):
        for j in range(m):
            if a[i][j]==x:
                print("Vi tri [",i,']','[',j,']',sep="")
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """
