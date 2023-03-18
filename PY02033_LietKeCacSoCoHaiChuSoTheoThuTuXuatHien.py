import re
s=input()
r='\d\d'
m={}
a=re.findall(r,s)
p={}
for x in a:
    if x not in p:
        print(x,end=' ')
        p[x]=1  