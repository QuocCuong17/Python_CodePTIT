class KhachHang:
    def __init__(self,maKH,tenKH,values):
        self.maKH='KH'+format(maKH,'02d')
        self.tenKH=tenKH
        va=values.split()
        loai=va[0]
        chiSoDau=int(va[1])
        chiSoCuoi=int(va[2])
        chiSo=chiSoCuoi-chiSoDau
        dinhMuc=0
        if loai=='A':
            dinhMuc+=100
        elif loai=='B':
            dinhMuc+=500
        elif loai=='C':
            dinhMuc+=200
        if(chiSo<dinhMuc):
            self.tienTrongDM=chiSo*450
        else:self.tienTrongDM=dinhMuc*450
        if(chiSo>dinhMuc):
            self.tienVuotDM=(chiSo-dinhMuc)*1000
        else: self.tienVuotDM=0
        self.VAT=self.tienVuotDM*0.05
        self.tongTien=self.tienTrongDM+self.tienVuotDM+self.VAT
    def chuan_hoa(self):
        tmp=self.tenKH.split()
        res=' '.join(tmp)
        res=res.title()
        self.tenKH=res
    def __str__(self):
        return '{:s} {:s} {:.0f} {:.0f} {:.0f} {:.0f}'.format(self.maKH,self.tenKH,self.tienTrongDM,self.tienVuotDM,self.VAT,self.tongTien)

if __name__ == '__main__':
    a=[]
    n=int(input())
    for i in range(n):
        kh= KhachHang(i+1,input(),input())
        kh.chuan_hoa()
        a.append(kh)
    a.sort(key=lambda x:-x.tongTien)
    print(*a,sep='\n')
