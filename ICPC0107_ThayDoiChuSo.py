if __name__ == '__main__':
    for t in range(int(input())):
        n,m=map(str,input().split())
        x1=input().strip()
        if x1.count(' '):
            x1,x2=x1.split()
        else:x2=input()
        p=max(n,m)
        q=min(n,m)
        print(int(x1.replace(p,q))+int(x2.replace(p,q)),end=' ')
        print(int(x1.replace(q,p))+int(x2.replace(q,p)))
