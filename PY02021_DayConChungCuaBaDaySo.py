if __name__ == '__main__':
    for t in range (int(input())):
        n,m,k = map(int,input().split())
        p1,p2,p3,ok=0,0,0,0
        a =[int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        c = [int(i) for i in input().split()]
        while p1 < n and p2 < m and p3 < k:
            if a[p1]==b[p2] and b[p2]==c[p3]:
                print(c[p3],end=' ')
                ok=1
                p1+=1
                p2+=1
                p3+=1
            elif a[p1]<b[p2]: p1+=1
            elif b[p2]<c[p3]: p2+=1
            elif c[p3]<a[p1]: p3+=1
        if ok: print()
        else:print('NO')

"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """