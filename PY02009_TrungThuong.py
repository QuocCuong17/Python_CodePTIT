if __name__ == '__main__':
    for t in range(int(input())):
        m={}
        n=int(input())
        for i in range(n):
            x=int(input())
            if x in m:
                m[x]+=1
            else:m[x]=1
        slxh=-1
        for i in m:
            if(m[i]>slxh):
                slxh=m[i]
                p=i
            elif m[i]==slxh:
                p=min(p,i)
        print(p)

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------