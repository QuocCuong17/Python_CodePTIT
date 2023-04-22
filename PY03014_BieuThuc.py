if __name__ == "__main__":
    test = int(input())
    for t in range(test):
        s = input()
        a = []
        cnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
                a.append(cnt)
                print(cnt, end=' ')
            elif s[i] == ')':
                print(a[-1], end=' ')
                a.pop()
        print()