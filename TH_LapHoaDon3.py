class HoaDon:
    def __init__(self,id, name, slm, donGia, chietKhau):
        self.id = id
        self.name = name
        self.slm = slm
        self.donGia = donGia
        self.chietKhau = chietKhau

    def get_tong_tien(self):
        return self.donGia*self.slm - self.chietKhau

    def __str__(self):
        return f'{self.id} {self.name} {self.slm} {self.donGia} {self.chietKhau} {self.get_tong_tien()}'

if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        hd = HoaDon(input(),input(),int(input()),int(input()),int(input()))
        a.append(hd)
    a=sorted(a, key=lambda x:-x.get_tong_tien())

    print(*a,sep='\n')

