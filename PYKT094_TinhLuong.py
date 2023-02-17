class PhongBan:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f'{self.name}'
class NhanVien:
    def __init__(self,id,name,wage,days,phongban):
        self.id = id
        self.name = name
        self.wage = wage
        self.days = days
        self.phongban=phongban
    def get_he_so(self):
        phanLoai=self.id[0]
        namCT=int(self.id[1:3])
        if phanLoai=='A':
            if namCT>=1 and namCT<=3:
                return 10
            elif namCT>=4 and namCT<=8:
                return 12
            elif namCT>=9 and namCT<=15:
                return 14
            else:return 20
        elif phanLoai=='B':
            if namCT>=1 and namCT<=3:
                return 10
            elif namCT>=4 and namCT<=8:
                return 11
            elif namCT>=9 and namCT<=15:
                return 13
            else:return 16
        elif phanLoai == 'C':
            if namCT >= 1 and namCT <= 3:
                return 9
            elif namCT >= 4 and namCT <= 8:
                return 10
            elif namCT >= 9 and namCT <= 15:
                return 12
            else:
                return 14
        elif phanLoai == 'D':
            if namCT >= 1 and namCT <= 3:
                return 8
            elif namCT >= 4 and namCT <= 8:
                return 9
            elif namCT >= 9 and namCT <= 15:
                return 11
            else:
                return 13
        return 0
    def get_luong_thang(self):
        return self.wage*self.days*self.get_he_so()*1000
    def __str__(self):
        return f'{self.id} {self.name} {self.phongban.name} {self.get_luong_thang()}'
if __name__ == '__main__':
    n = int(input())
    pb,nv=[],[]
    for i in range(n):
        s=input()
        p=PhongBan(s[:2],s[3:])
        pb.append(p)
    m = int(input())
    for i in range(m):
        s=input()
        id=s[3:5]
        for j in pb:
            if j.id==id:
                n=NhanVien(s,input(),int(input()),int(input()),j)
                nv.append(n)
    print(*nv,sep='\n')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """