if __name__ == "__main__":
    for __ in range(int(input())):
        s=input()
        sum, t = 0, 1
        for i in range(0, len(s)):
            if i%2 == 0:
                t=t*int(s[i])
            else:sum+=int(s[i])
        if sum == 0:
            print("INVALID")
        else:
            print("{:.6f}".format(t / sum))
"""
2
1012
30304
"""