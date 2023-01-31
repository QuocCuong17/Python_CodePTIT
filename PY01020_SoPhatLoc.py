def check(s):

    for i in range(1,len(s)+1):
        if(s[len(s)-1]=='6' and s[len(s)-2]=='8'):
            return 'YES'
    return 'NO'
for t in range ( int(input())):
    s = input()
    print(check(s))