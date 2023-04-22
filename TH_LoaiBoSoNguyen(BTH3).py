f = open("DATA.in",'r')
a=[]
ghd=-2147483648
ght=2147483647
for j in f:
    for i in j.split():
        if not i.isdigit() :
            a.append(i)
        if i.isdigit():
            if int(i)>ght:
                a.append(i)
            if int(i)<ghd:
                a.append(i)
print(*sorted(a))
