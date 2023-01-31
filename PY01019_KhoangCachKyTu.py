def check(s1,s2):
    for i in range(1,len(s)):
        if(abs(ord(s1[i])-ord(s1[i-1]))!=abs(ord(s2[i])-ord(s2[i-1]))):
            return False
    return True
for t in range (int(input())):
    s=input()
    if(check(s,s[::-1])):
        print("YES")
    else:print("NO")