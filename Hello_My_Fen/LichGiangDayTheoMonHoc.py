class MonHoc:
    def __init__(self,id,name,soTC):
        self.id = id
        self.name = name
        self.soTC = soTC
    def __str__(self):
        return f'{self.name}'
class LichGD:
    def __init__(self,id,idM,thu,kip,name,phong):
        self.id = "HP"+format(id,"03d")
        self.idM = idM
        self.thu = thu
        self.kip = kip
        self.name = name
        self.phong = phong
    def __str__(self):
        return f'{self.id} {self.thu} {self.kip} {self.name} {self.phong}'

if __name__ == "__main__":
    mh,gd = [],[]
    n = int(input())
    for i in range(n):
        mh.append(MonHoc(input(),input(),int(input())))
    m = int(input())
    for i in range(m):
        mon =''
        id = input()
        thu = input()
        kip = input()
        name = input()
        phong = input()
        for j in mh:
            if j.id == id:
                mon=j
                break
        gd.append(LichGD(i+1,id,thu,kip,name,phong))
    gd.sort(key=lambda x:(x.thu,x.kip,x.name))
    s = input()
    for i in gd:
        for j in mh:
            if i.idM == j.id and i.idM == s:
                print("LICH GIANG DAY MON ",j.name,':',sep='')
                break
        break

    for i in gd:
        if i.idM == s:
            print(i)
"""
2
INT1155
Tin hoc co so 2
2
INT13162
Lap trinh voi Python
3
4
INT13162
5
1
Nguyen Hoang Anh
102-A2
INT1155
3
1
Nguyen Dinh Hien
201A-A3
INT1155
4
1
Nguyen Quy Sy
201A-A3
INT1155
5
1
Tran Quy Nam
201A-A3
INT1155
"""
