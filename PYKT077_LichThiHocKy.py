from datetime import datetime,date
class MonHoc:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f'{self.id} {self.name}'
class CaThi:
    def __init__(self,id,idmh,ngayThi,gioThi,nhomThi):
        self.id='T'+format(id,'03d')
        self.nhomThi=nhomThi
        self.idmh=idmh
        self.ngayThi=ngayThi
        self.gioThi=gioThi
    def __str__(self):
        return f'{self.id} {str(self.idmh)} {self.ngayThi} {self.gioThi} {self.nhomThi}'

if __name__ == '__main__':
    n,m=map(int,input().split())
    M,C=[],[]
    for i in range(n):
        mh=MonHoc(input(),input())
        M.append(mh)
    for i in range(m):
        s=input().split()
        idmh=s[0]
        for j in M:
            if j.id==idmh:
                ct=CaThi(i+1,j,s[1],s[2],s[3])
                C.append(ct)
                break
    C.sort(key=lambda x:(datetime.strptime(x.ngayThi,'%d/%m/%Y'),datetime.strptime(x.gioThi,'%H:%M'),x.id))
    print(*C,sep='\n')

