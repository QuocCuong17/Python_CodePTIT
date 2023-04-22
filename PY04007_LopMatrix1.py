t = int(input())
for test in range(t):
    n,m=map(int,input().split())
    a= [[0]*m]*n
    b=[]
    for i in range(n):
        a[i]=[int(x) for x in input().split()]
    for i in range(m):
        x=[]
        for j in range(n):
            x.append(a[j][i])
        b.append(x)
    for i in range(n):
        for j in range(n):
            res = 0
            for k in range(m):
                res += (a[i][k]*b[k][j])
            print(res,end=' ')
        print()