import math
n , k = map(int,input().split())
lower,upper=10**(k-1),10**k
dem=0
for i in range(lower,upper,1):
    if math.gcd(n,i)== 1:
        print(i,end=' ')
        dem+=1
        if(dem%10==0):print()