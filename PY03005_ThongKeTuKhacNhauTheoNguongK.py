if __name__ == "__main__":
    mp = {}
    n,m = map(int,input().split())
    for i in range(n):
        s=input().lower()
        for j in range(len(s)):
            if not s[j].isalnum() and not s[j].isdigit():
                s = s.replace(s[j],' ')
        for j in s.split():
            if j in mp:
                mp[j]+=1
            else:mp[j]=1
    mp = sorted(mp.items(), key=lambda x: (-x[1],x[0]))
    for a,b in mp:
        if b>=m:
            print(a,' ',b,sep='')