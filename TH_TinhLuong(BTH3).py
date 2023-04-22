class PhongBan:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return f'{self.name}'
class NhanVien:
    def __init__(self,id,name,luongCB,soNgay,phongBan):
        self.id = id
        self.name = name
        self.luongCB = luongCB
        self.soNgay = soNgay
        self.phongBan = phongBan
    def get_he_so(self):
        pl=self.id[0]
        namCT = int(self.id[1:3])
        if pl == 'A':
            if namCT>=16:
                return 20
            elif namCT>=9:
                return 14
            elif namCT>=4:
                return 12
            elif namCT>=1:
                return 10
        elif pl =='B':
            if namCT>=16:
                return 16
            elif namCT>=9:
                return 13
            elif namCT>=4:
                return 11
            elif namCT>=1:
                return 10
        elif pl =='C':
            if namCT>=16:
                return 14
            elif namCT>=9:
                return 12
            elif namCT>=4:
                return 10
            elif namCT>=1:
                return 9
        elif pl =='D':
            if namCT>=16:
                return 13
            elif namCT>=9:
                return 11
            elif namCT>=4:
                return 9
            elif namCT>=1:
                return 8
    def get_luong_thang(self):
        return self.luongCB*self.soNgay*self.get_he_so()*1000
    def __str__(self):
        return f'{self.id} {self.name} {self.phongBan} {self.get_luong_thang()}'

if __name__ == "__main__":
    pb,nv=[],[]
    n = int(input())
    for i in range(n):
        s=input()
        p=PhongBan(s[:2],s[3:])
        pb.append(p)
    m = int(input())
    for i in range(m):
        s=input()
        s1=s[3:5]
        for j in pb:
            if j.id == s1:
                v = NhanVien(s,input(),int(input()),int(input()),j)
                nv.append(v)
    print(*nv,sep='\n')

"""
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
"""