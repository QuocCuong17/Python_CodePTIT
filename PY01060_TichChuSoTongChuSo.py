for t in range(int(input())):
    tich=1
    tong=0
    s=input()
    for i in range(len(s)):
        if(i%2==0):
            if s[i] != '0':
                tich=tich*int(s[i])
        else:
            tong=tong+int(s[i])
    print(tich,' ',tong)