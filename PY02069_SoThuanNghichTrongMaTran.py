def stn(n):
    if len(n)<2: return False
    if n != n[::-1]: return False
    return True
if __name__ == '__main__':
    n , m = map(int,input().split())
    a=[]
    x=0
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    b=[i for x in a for i in x]
    for i in range(n):
        for j in range(m):
            if stn(str(a[i][j])) and a[i][j]>x:
                x=a[i][j]
    if x==0:print("NOT FOUND")
    else:print(x)
    for i in range(n):
        for j in range(m):
            if x==a[i][j]:
                print("Vi tri [",i,'][',j,']',sep="")