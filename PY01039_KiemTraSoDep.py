def check(s):
    for i in range(0,len(s)-2):
        if(s[i]!=s[i+2]):
            return 'NO'
    return 'YES'
for t in range(int(input())):
    n = (input())
    print(check(n))

