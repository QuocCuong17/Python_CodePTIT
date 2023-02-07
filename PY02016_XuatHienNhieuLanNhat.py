if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        m={}
        a=[int(i) for i in input().split()]
        for i in a:
            if i in m:
                m[i]+=1
            else:m[i]=1
        slxh=0
        for i in m:
            if slxh < m[i]:
                slxh=m[i]
                p=i
            elif m[i]==slxh:
                p=min(p,i)
        if slxh > n/2:
            print(p)
        else:print('NO')
#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------