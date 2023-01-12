s=input()
cnt=0
for x in s:
    if(x>='a' and x<='z'):
        cnt+=1
if(cnt>len(s)-cnt):
    print(s.lower())
else:print(s.upper())