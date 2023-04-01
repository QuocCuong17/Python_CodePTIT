def generate_string(n):
    if n == 1:
        return "A"
    else:
        prev_str = generate_string(n - 1)
        new_char = chr(ord('A') + n - 1)
        return prev_str + new_char + prev_str

if __name__ == "__main__":
    test=int(input())
    for i in range(test):
        n,k = map(int,input().split())
        s = generate_string(n)
        print(s[k - 1])