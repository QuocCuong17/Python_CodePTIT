from datetime import datetime
class TheLoai:
    def __init__(self,maTL,tenTL):
        self.maTL='TL'+format(maTL,'03d')
        self.tenTL=tenTL
    def __str__(self):
        return self.tenTL
class Phim:
    def __init__(self,maPhim,theLoai,ngayKC,tenPhim,tapPhim):
        self.maPhim='P'+format(maPhim,'03d')
        self.theLoai=theLoai
        self.ngayKC=ngayKC
        self.tapPhim=tapPhim
        self.tenPhim=tenPhim
    def __str__(self):
        return f'{self.maPhim} {self.theLoai} {self.ngayKC} {self.tenPhim} {self.tapPhim}'

if __name__ == '__main__':
    t,p=[],[]
    n,m=map(int,input().split())
    for i in range(n):
        s=input()
        tl=TheLoai(i+1,s)
        t.append(tl)
    for i in range(m):
        s=input()
        for j in (t):
            if j.maTL==s:
                phim=Phim(i+1,j,input(),input(),int(input()))
                p.append(phim)
    p.sort(key=lambda x:(datetime.strptime(x.ngayKC, '%d/%m/%Y'),x.tenPhim,-x.tapPhim))
    print(*p,sep='\n')
"""
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
"""