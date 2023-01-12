t = int(input())
while t >0:
    t-=1
    s = input()
    n1=int(s[0]+s[1])
    n2=int(s[len(s)-2]+s[len(s)-1])
    if(n1==n2): print("YES")
    else:print("NO")