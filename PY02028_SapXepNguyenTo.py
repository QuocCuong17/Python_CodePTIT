import math
def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

if __name__ == '__main__':
    te = int(input())
    a=[int(i) for i in input().split()]
    n,m,ok=[],[],[0]*te
    for i in range(len(a)):
        if snt(int(a[i])):
            n.append(a[i])
            ok[i]=1
        else:m.append(a[i])
    n.sort()
    i,j=0,0
    for k in range(te):
        if ok[k]:
            print(n[i],end=' ')
            i+=1
        else:
            print(m[j],end=' ')
            j+=1
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """