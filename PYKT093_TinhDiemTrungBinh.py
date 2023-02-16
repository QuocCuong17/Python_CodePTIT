import math


class SinhVien:
    def __init__(self,maSV,tenSV,d1,d2,d3):
        self.maSV="SV"+format(maSV,'02d')
        self.tenSV=tenSV
        self.tongDiem=math.ceil((d1*3+d2*3+d3*2)/8*100)/100
    def chuan_hoa(self):
        tmp=self.tenSV.split()
        res=' '.join(tmp)
        res=res.title()
        self.tenSV=res
    def __str__(self):
        return '{:s} {:s} {:.2f} {:d}'.format(self.maSV,self.tenSV,self.tongDiem,self.rank)
if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(n):
        sv = SinhVien(i+1,input().strip(),float(input()),float(input()),float(input()))
        sv.chuan_hoa()
        a.append(sv)
    list=[]
    a.sort(key=lambda x:(-x.tongDiem, x.maSV))
    a[0].rank=1
    for i in range(1,len(a)):
        a[i].rank=a[i-1].rank if a[i].tongDiem==a[i-1].tongDiem else i+1
    print(*a,sep='\n')
