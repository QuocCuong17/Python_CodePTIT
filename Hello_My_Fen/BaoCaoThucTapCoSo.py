class SinhVien:
    def __init__(self,id,name,phone,mail):
        self.id = id
        self.name = name
        self.phone = phone
        self.mail = mail
    def __str__(self):
        return f'{self.id} {self.name}'
class DeTai:
    def __init__(self,id,nameT,nameD):
        self.id = "DT"+format(id,"03d")
        self.nameT = nameT
        self.nameD = nameD
    def __str__(self):
        return f"{self.nameD} {self.nameT}"
class HoiDong:
    def __init__(self,idS,idD,idH):
        self.idS = idS
        self.idD = idD
        self.idH = idH
        self.sttHD = int(self.idH[-1])
        # print(self.sttHD)
    def __str__(self):
        return f'{self.idS} {self.idD}'

if __name__ == "__main__":
    sv,dt,hd,a=[],[],[],[]
    n = int(input())
    for __ in range(n):
        sv.append(SinhVien(input(),input(),input(),input()))
    m = int(input())
    for i in range(m):
        dt.append(DeTai(i+1,input(),input()))
    k = int(input())
    for i in range(k):
        hi = input().split()
        idS = hi[0]
        idD = hi[1]
        idH = hi[2]
        if idH not in a:
            a.append(idH)
        sinh,de = '',''
        for j in sv:
            if j.id == idS:
                sinh = j
                break
        for j in dt:
            if j.id == idD:
                de = j
                break
        hd.append(HoiDong(sinh,de,idH))
    hd.sort(key=lambda x:(x.idS.id))
    for i in range(len(a)):
        print("DANH SACH HOI DONG ",i+1,":",sep='')
        for j in hd:
            if j.sttHD == i+1:
                print(j)

"""
2
B19DCCN999
Ngo Quang Huy
0976544443
B19DCCN999@stu.ptit.edu.vn
B19DCCN997
Nguyen Manh Cuong
0987654321
B19DCCN997@stu.ptit.edu.vn
3
Nguyen Hoai Nam
Xay dung website tim kiem nha thong minh
Tran Thanh Cong
Xay dung he thong diem danh bang nhan dang van tay
Le Thi My Uyen
Xay dung website cap nhat tin tuc
2
B19DCCN997 DT001 HD2
B19DCCN999 DT002 HD1
"""
