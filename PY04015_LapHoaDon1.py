from functools import cmp_to_key
class HoaDon1:
    def __init__(self,maKH,tenKH,chiSoCu,chiSoMoi):
        self.maKH='KH'+format(maKH,'02d')
        self.tenKH=tenKH
        self.chiSoCu=chiSoCu
        self.chiSoMoi=chiSoMoi
    def soKhoi(self):
        return self.chiSoMoi-self.chiSoCu
    def tongTien(self):
        hi=0
        if self.soKhoi()>100:
            hi= (50*100+150*50+(self.soKhoi()-100)*200)*1.05
        elif self.soKhoi()>50:
            hi= (50*100+(self.soKhoi()-50)*150)*1.03
        elif self.soKhoi()>=0:
            hi= self.soKhoi()*1.02*100
        return round(hi)
    def __str__(self):
        return f'{self.maKH} {self.tenKH} {self.tongTien()}'
def cmp(a,b):
    o1,o2=a.tongTien(),b.tongTien()
    if o1!=o2:
        return o2-o1
if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(n):
        h=HoaDon1(i+1,input(),int(input()),int(input()))
        a.append(h)
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x)