import math


def khoangCach(v1,v2):
    kc = math.sqrt(sum((x-y)**2 for x, y in zip(v1,v2)))
    return '{:.2f}'.format(kc)

def tichVoHuong(v1,v2):
    tvh = (sum(x*y for x,y in zip(v1,v2)))
    return '{:.0f}'.format(tvh)

for __ in range(int(input())):
    v1 = list(map(float,input().split()))
    v2 = list(map(float, input().split()))
    if len(v1) != len(v2):
        print("Invalid")
    else:
        print(khoangCach(v1,v2),tichVoHuong(v1,v2),sep=' ',end='\n')
'''
Input:
3
10 40 20 30
2 4 -5 3
2 4 6 8
5 10 -15 20
1 1
0 0 
output:
52.10 170
25.10 120
1.41 0
'''