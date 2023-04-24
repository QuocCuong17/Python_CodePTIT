class Inf:
    def __init__(self,bienSo,loaiXe,soGhe,huongDi,ngayDC):
        self.huongDi = huongDi
        self.ngayDC = ngayDC
        self.bienSo = bienSo
        self.loaiXe = loaiXe
        self.soGhe = soGhe
        self.price=0
        if self.huongDi == 'OUT':   self.price += 0
        else:
            if self.loaiXe == 'Xe_con' and int(self.soGhe) == 5:    self.price += 10000
            if self.loaiXe == 'Xe_con' and int(self.soGhe) == 7:    self.price += 15000
            if self.loaiXe == 'Xe_tai' and int(self.soGhe) == 2:    self.price += 20000
            if self.loaiXe == 'Xe_khach' and int(self.soGhe) == 29:    self.price += 50000
            if self.loaiXe == 'Xe_khach' and int(self.soGhe) == 45:    self.price += 70000
    def __str__(self):
        return f'{self.ngayDC}: {self.price}'
a=[]
def inList(s):
    for i in a:
        if i.ngayDC == s.ngayDC:
            i.price += s.price
            return
    a.append(s)

if __name__ == "__main__":
    for t in range(int(input())):
        s = input().split()
        dt = Inf(s[0],s[1],(s[2]),s[3],s[4])
        inList(dt)
    print(*a,sep='\n')

"""
5
30F-123.15 Xe_con 5 OUT 06/11/2021
30F-123.15 Xe_con 5 IN 06/11/2021
30H-123.15 Xe_con 7 IN 06/11/2021
29H-222.68 Xe_tai 2 IN 07/11/2021
30G-511.15 Xe_con 5 IN 07/11/2021
"""