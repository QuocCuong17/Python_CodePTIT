import math

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())*2
        a=[]
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0 and (n//i-i)&1==1:
                a+=[i]
        print(len(a))