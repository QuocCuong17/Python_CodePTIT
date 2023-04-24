m={}
for t in range(int(input())):
    s = input().lower()
    for i in range(len(s)):
        if (not s[i].isdigit() and not s[i].isalnum()) or s[i].isdigit():
            s = s.replace(s[i],' ')
    for i in s.split():
        if i in m:
            m[i]+=1
        else:m[i]=1
m = sorted(m.items(),key= lambda x:(-x[1],x[0]))
for a,b in m:
    print(a,' ',b)

"""
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""