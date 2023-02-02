def check(s):
    for i in range(1000):
        if(s%7==0): return s
        dao=int(str(s)[::-1])
        s+=dao
    return -1
for t in range (int(input())):
    s=(int)(input())
    print(check(s))

