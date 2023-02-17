if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    k={}
    maxx,x,tmp=10**-10,0,0
    for i in a:
        if i in k:
            k[i]+=1
        else:k[i]=1
        maxx=max(maxx,k[i])
    for i in range(1,m+1):
        if i in k and k[i]>x and k[i]!=maxx:
            x=k[i]
            tmp=i
    if tmp==0:
        print('NONE')
    else:print(tmp)