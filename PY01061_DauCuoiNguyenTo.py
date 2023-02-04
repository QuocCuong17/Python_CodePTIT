import math


def snt(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return True

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        n=int(s[-3:])
        m=int(s[0:3])
        if(snt(n) and snt(m)):
            print('YES')
        else:print('NO')