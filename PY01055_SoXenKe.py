def check(s):
    if(len(s)%2==0):return 'NO'
    for i in range(len(s)):
        if(s[0]==s[1]): return 'NO'
        if(s[0]!=s[2]!=s[4]!=s[len(s)-1]):return 'NO'
    return 'YES'
for t in range(int(input())):
    s=input()
    print(check(s))