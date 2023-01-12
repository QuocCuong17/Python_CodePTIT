t=(int)(input())
while t>0:
    t-=1
    n = input()
    s4=n.count('4')
    s7=n.count('7')
    if(s4+s7==len(n)): print("YES")
    else:print("NO")

"""3
4477
44444487777777777
47474747474777777777777744444"""