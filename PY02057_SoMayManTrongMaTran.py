if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    maxMT,minMT=10**-5,10**5
    b=[i for x in a for i in x]
    maxMT=max(b)
    minMT=min(b)
    disT=maxMT-minMT
    x,ok=0,0
    for i in range(n):
        for j in range(m):
            if a[i][j]==disT:
                x=a[i][j]
                ok=1
    if ok==0:print('NOT FOUND')
    else:print(x)
    for i in range(n):
        for j in range(m):
            if a[i][j]==x:
                print("Vi tri [",i,'][',j,']',sep="")