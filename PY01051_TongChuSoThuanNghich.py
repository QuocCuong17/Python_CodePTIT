def check(s):
    S= str(sum(int(i)for i in s))
    if(len(S)<2 or S!=S[::-1]): return 'NO'
    return "YES"
for t in range(int(input())):
    s= input()
    print(check(s))
