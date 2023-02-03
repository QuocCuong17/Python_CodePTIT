import math


def snt(n):
    if n < 2: return False
    for i in range (2,int(math.sqrt(n)+1)):
        if(n%i==0): return False
    return True


def checkal(s):
    for i in s:
        if not snt(int(i)):
            return 'No'
    if not snt(int(s)) or not snt(int(s[::-1])):
        return 'No'
    return 'Yes'


for t in range(int(input())):
    s = input()
    print(checkal(s))