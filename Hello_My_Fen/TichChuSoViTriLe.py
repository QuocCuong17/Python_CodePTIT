if __name__ == "__main__":
    for __ in range(int(input())):
        s = input()
        tich = 1
        ok=0
        for i in range(0,len(s),2):
            if s[i] != '0':
                tich *= int(s[i])
            if s[i] == '1':
                ok=1
        if tich == 1:
            if ok:
                print("1")
        else:
            print(tich)
'''
2
123410
123456789123456789
'''