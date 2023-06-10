def check(s):
    d = s.count("3")+s.count("5")
    if d != 3 and d != 5:
        return "NO"
    return "YES"

if __name__ == "__main__":
    print(check(input()))