if __name__ == '__main__':
    for t in range(int(input())):
        n=input()
        a=input().split()
        m={}
        for i in a:
            if i in m:
                m[i]+=1
            else:m[i]=1
        for i in m:
            if m[i]%2==1:
                print(i)
