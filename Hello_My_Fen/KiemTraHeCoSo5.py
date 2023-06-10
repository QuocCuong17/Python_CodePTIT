def check(s):
    for i in s:
        if i not in '01234':
            return False
    sum = 0
    for i in s:
        sum += int(i)
    if sum != 5:
        return False
    return True

for __ in range(int(input())):
    if check(input()):
        print("YES")
    else:
        print("NO")

'''
3
1214AB
102101
2222222222
'''