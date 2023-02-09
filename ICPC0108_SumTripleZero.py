for t in range(int(input())):
    n = int(input())
    a=[int(i) for i in input().split()]
    a=sorted(a)
    cnt=0
    for i in range(0,n-2):
        l=i+1
        r=len(a)-1
        while l<r:
            if a[i]+a[l]+a[r]==0:
                cnt+=1
                l+=1
            elif a[i]+a[l]+a[r]<0:
                l+=1
            else:r-=1
    print(cnt)
