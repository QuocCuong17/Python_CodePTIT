import math

n = input()
a=[int(i) for i in input().split()]
a.sort()
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if math.gcd(a[i],a[j])==1:
            print(a[i]," ",a[j])