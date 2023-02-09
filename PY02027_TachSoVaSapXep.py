a=[]
for t in range(int(input())):
   s=input()
   s=s+'z'
   x=0
   for i in range(len(s)):
       if s[i].isdigit():
           x=x*10+int(s[i])
       else:
           if s[i-1].isdigit():
               a.append(x)
               x=0
a=sorted(a)
for i in a:
    print(i)