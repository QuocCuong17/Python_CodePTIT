import math
res, n = 0, int(input())
m = int(math.sqrt(n)) + 1

p = [i for i in range(m)]
for i in range(2, int(math.sqrt(m))):
    if p[i] == i:
        for j in range(i*i, m, i):
            if p[j] == j: p[j] = i

for i in range(2,m):
    i1 = p[i]
    i2 = i // i1
    if i2 == p[i//i1] and i1 != i2 and i2 != 1:
        res += 1
    elif p[i] == i and pow(i, 8) <= n:
        res += 1

print(res)