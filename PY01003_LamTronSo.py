t = (int)(input())

while (t > 0):
    t -= 1
    n = input()
    if int(n) < 10:
        print(n)
    else:
        size = len(n)  # chiều dài xâu
        s = list(n)  # Lưu các ký tự trong xâu n
        for i in range(size - 1, 0, -1):
            if int(s[i]) >= 5:
                s[i - 1] = str(int(s[i - 1]) + 1)
            s[i] = '0'
        print("".join(s))  # tạo lặp lại, nối các thành phần thành 1 chuỗi
