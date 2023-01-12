s=input()
a=list(s)
s4=0
s7=0
for i in range(0, len(s)):
    if(a[i]=='4') : s4+=1
    if(a[i]=='7'): s7+=1
if(s4+s7==4 or s4+s7==7): print("YES")
else: print("NO")

"""s=input()
s4=s.count('4')
s7=s.count('7')
if s4+s7==4 or s4+s7==7: print("YES")
else:print("NO")"""