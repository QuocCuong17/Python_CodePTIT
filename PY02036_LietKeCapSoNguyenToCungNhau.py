import math

if __name__ == '__main__':
    t = input()
    a=[int(i) for i in input().split()]
    a.sort()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(math.gcd(a[i],a[j])==1):
                print(a[i]," ",a[j])