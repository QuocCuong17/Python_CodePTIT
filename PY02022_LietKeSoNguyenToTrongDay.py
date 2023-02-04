import math


def snt(n):
    if n < 2 : return False
    for i in range (2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    m={}
    t = input()
    a=[int(i) for i in input().split()]
    for i in a:
        if snt(i):
            if i in m:
                m[i]+=1
            else:m[i]=1
    for i in m:
        print(str(i)+" "+str(m[i]))