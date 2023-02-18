if __name__ == '__main__':
    n = int(input())
    size=0
    a,chan,le,ok=[],[],[],[0]*n
    while len(a)<n:
        a+=[int(i) for i in input().split()]
    for i in range(n):
        if a[i] % 2 ==0:
            ok[i]=1
            chan.append(a[i])
        else:
            le.append(a[i])
    chan.sort()
    le=sorted(le,reverse=True)
    i,j=0,0
    for k in range(n):
        if ok[k]:
            print(chan[i],end=' ')
            i+=1
        else:
            print(le[j],end=' ')
            j+=1
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """