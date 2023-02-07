f='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    N,b=map(int,input().split())
    res=''
    while(N>0):
        res=f[N%b]+res
        N=int(N/b)
    print(res)
#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------