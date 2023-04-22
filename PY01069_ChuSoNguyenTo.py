ans='2357'
l=[]
def valid(s):
    for i in ans:
        if s.count(i) == 0:
            return False
    return s[-1]!='2'
def Try(i,s,n):
    if i>=4 and i<=n and valid(s):
        l.append(int(s))
    if i <n :
        for c in ans:
            Try(i+1,s+c,n)
Try(0,'',int(input()))
print(*sorted(l),sep='\n')