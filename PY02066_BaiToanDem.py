if __name__ == '__main__':
    n = int(input())
    a=[]
    while len(a)<n:
        i = [int(i) for i in input().split()]
        a+=i
    m = {}
    last=0
    check=1
    for i in a :
        m[i]=1
        last=max(last,i)
    for i in range(1,last+1):
        if(not i in m):
            print(i)
            check=0
    if check: print('Excellent!')
