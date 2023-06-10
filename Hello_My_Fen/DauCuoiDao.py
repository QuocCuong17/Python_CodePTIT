for __ in range(int(input())):
    s = input()
    a=s[:2]
    b=s[-2:]
    a=a[::-1]
    b=b[::-1]
    s1=b+s[2:-2]+a
    if s == s1:
        print("YES")
    else:print("NO")

'''
5
12321
1234512
1023321111111
1923232323232391
89123123198
'''