a,k,n = map(int,input().split())
bMin = (int(a/k)+1)*k-a
bMax = int(n/k)*k-a
if bMin <= bMax:
    for i in range(bMin,bMax+1,k):
        print(i,end=' ')
else: print("-1")