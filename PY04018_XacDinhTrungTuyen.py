class GiangVien:
    def __init__(self,maGV,tenGV,maXT,diemTH,diemCM):
        self.maGV='GV'+format(maGV,'02d')
        self.tenGV=tenGV
        res1=maXT[0]
        res2=maXT[1]
        self.diemTH=diemTH
        self.diemCM=diemCM
        diemUT=0
        if res1=='A':
            self.tenMH='TOAN'
        elif res1=='B':
            self.tenMH='LY'
        elif res1=='C':
            self.tenMH='HOA'
        if res2=='1':
            diemUT+=2
        elif res2=='2':
            diemUT+=1.5
        elif res2=='3':
            diemUT+=1
        self.tongDiem=self.diemTH*2+self.diemCM+diemUT
        if self.tongDiem>=18:
            self.ketQua="TRUNG TUYEN"
        else:self.ketQua="LOAI"
    def __str__(self):
        return self.maGV+" "+self.tenGV+" "+self.tenMH+" "+'{:.1f}'.format(self.tongDiem)+" "+self.ketQua
if __name__ == '__main__':
    n = int(input())
    a=[]
    for i in range(n):
        gv = GiangVien(i+1,input(),input(),float(input()),float(input()))
        a.append(gv)
    a.sort(key=lambda x:-x.tongDiem)
    for x in a:
        print(x)
