def check(s):
    if s[-3:] == '668':
        return "YES"
    else:
        return "NO"
for __ in range(int(input())):
    print(check(input()))

'''2
123456
1111668'''
