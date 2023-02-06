a=[0]*1000001
def sang():
    a[0]=a[1]=1
    for i in range(2,1000):
        if a[i]==0:
            for j in range(i*i,1000001,i):
                a[j]=1

if __name__ == '__main__':
    sang()
    for t in range(int(input())):
        n=int(input())
        cnt=0
        for i in range(6,n):
            if a[i]==0 and a[i-6]==0 and (a[i-2]==0 or a[i-4]==0):
                cnt+=1
        print(cnt)

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------