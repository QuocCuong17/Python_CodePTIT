import math


def snt(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for __ in range(int(input())):
    a, b = map(int,input().split())
    m = math.gcd(a,b)
    s = 0
    m = str(m)
    for i in m:
        s += int(i)
    if snt(s):
        print("YES")
    else: print("NO")