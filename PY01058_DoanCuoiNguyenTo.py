import math


def snt(n):
    if n<2: return 'NO'
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    for t in range (int(input())):
        s = input()
        n=int(s[-4:])
        print(snt(n))