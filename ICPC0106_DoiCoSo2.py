f='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def doiCS(n,b):
    res=''
    while(n>0):
        res+=f[n%b]
        n//=b
    return res[::-1]
for t in range(int(input())):
    N=int(input())
    b=int(input(),2)
    print(doiCS(b,N))