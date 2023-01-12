import math
t = int(input())
while t > 0:
    t -= 1
    n, x, m = map(float, input().split())
    # tong = n*(1+x%)^a=m => a?
    res = math.log(m/n, 1+x/100)
    val = int(res)
    if res > val:
        val += 1
    print(val)