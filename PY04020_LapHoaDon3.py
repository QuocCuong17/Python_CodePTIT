class HoaDon:
    def __init__(self,maMH,tenMH,slMua,donGia,chietKhau):
        self.maMH=maMH
        self.tenMH=tenMH
        self.slMua=slMua
        self.donGia=donGia
        self.chietKhau=chietKhau
        self.tongTien=donGia*slMua-chietKhau
    def __str__(self):
        return self.maMH+" "+self.tenMH+" "+str(self.slMua)+" "+str(self.donGia)+" "+str(self.chietKhau)+" "+str(self.tongTien)

if __name__ == '__main__':
    a=[]
    n =int(input())
    for i in range(n):
        hd=HoaDon(input(),input(),int(input()),int(input()),int(input()))
        a.append(hd)
    a.sort(key=lambda x:-x.tongTien)
    for x in a:
        print(x)
