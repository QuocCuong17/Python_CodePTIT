from datetime import datetime
from functools import cmp_to_key
class HoaDon2:
    def __init__(self,maKH,tenKH,soPhong,ngayNhan,ngayTra,tienDV):
        self.maKH='KH'+format(maKH,'02d')
        self.tenKH=tenKH
        self.soPhong=soPhong
        time=datetime.strptime(ngayTra,'%d/%m/%Y') -datetime.strptime(ngayNhan,'%d/%m/%Y')
        self.soNgay=time.days+1
        self.tienDV=tienDV
    def gia(self):
        if self.soPhong[0]=='1':
            return 25
        elif self.soPhong[0]=='2':
            return 34
        elif self.soPhong[0]=='3':
            return 50
        else: return 80
    def thanhTien(self):
        return self.soNgay*self.gia()+self.tienDV
    def __str__(self):
        return f'{self.maKH} {self.tenKH} {self.soPhong} {self.soNgay} {self.thanhTien()}'
def cmp(a,b):
    o1,o2=a.thanhTien(),b.thanhTien()
    if o1!=o2:
        return o2-o1
if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(n):
        h=HoaDon2(i+1,input().strip(),input().strip(),input().strip(),input().strip(),int(input().strip()))
        a.append(h)
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x)