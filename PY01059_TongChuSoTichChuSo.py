for t in range(int(input())):
    sum=0
    tich=1
    s=input()
    for i in range(len(s)):
        if(i%2==0):
            sum=sum+int(s[i])
        else:
            if s[i]!= '0' :
                tich*=int(s[i])
    if tich == 1:tich=0
    print(sum," ",tich)
