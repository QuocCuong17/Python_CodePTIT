if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int,input().split()))
        a.append(b)
    k = int(input())
    st,sd=0,0
    for i in range(n):
        for j in range(n):
            if i < j : st+=a[i][j]
            elif j < i : sd+=a[i][j]
    s=abs(st-sd)
    if s <= k:
        print('YES')
        print(s)
    else:
        print('NO')
        print(s)
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """