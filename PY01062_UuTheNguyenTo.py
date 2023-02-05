import math


def snt(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0 : return False
    return True
def check(s):
    if(not snt(int(len(s)))): return 'NO'
    cnt =0
    for i in s:
        if(snt(int(i))): cnt+=1
    if(cnt<=len(s)-cnt): return 'NO'
    return 'YES'
for t in range(int(input())):
    s=input()
    print(check(s))