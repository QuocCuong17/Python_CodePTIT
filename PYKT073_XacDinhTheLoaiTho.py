if __name__ == '__main__':
    n=int(input())
    lst=[(input().split())for i in range(n)]
    i=0
    a=[]
    while i < n:
        if len(lst[i])==7:
            i+=4
            a+=[2]
        elif len(lst[i])==6:
            i+=2
            a+=[1]
            while i < n and len(lst[i])==6:
                i+=2
    print(len(a),*a,sep='\n')
