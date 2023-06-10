def find(s1,s2):
    a = []
    for i in range(len(s1)-len(s2)+1):
        if s1[i:i+len(s2)] == s2:
            a.append(i+1)
    return a

if __name__ == "__main__":
    for __ in range(int(input())):
        s1, s2 = input(), input()
        for x in find(s1, s2):
            print(x, end=' ')
        print()
"""
2
aaaaa
aa
abcde
bc
"""