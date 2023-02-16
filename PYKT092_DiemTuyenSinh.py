class ThiSinh:
    def __init__(self,id,name,score,nation,local):
        self.id='TS'+format(id,'02d')
        self.name=name
        self.score=score
        self.nation=nation
        self.local=local
        diemKV,diemDT=0,0
        if local=='1':
            diemKV+=1.5
        elif local=='2':
            diemKV+=1
        if nation != 'Kinh':
            diemDT+=1.5
        self.tongDiem=self.score+diemKV+diemDT
        if self.tongDiem>=20.5:
            self.trangThai='Do'
        else:self.trangThai='Truot'
    def chuan_hoa(self):
        tmp=self.name.split()
        res=' '.join(tmp)
        res=res.title()
        self.name=res
    def __str__(self):
        return '{:s} {:s} {:.1f} {:s}'.format(self.id,self.name,self.tongDiem,self.trangThai)
if __name__ == '__main__':
    a=[]
    n=int(input())
    for i in range(n):
        ts =ThiSinh(i+1,input(),float(input()),input(),input())
        ts.chuan_hoa()
        a.append(ts)
    a.sort(key=lambda x:(-x.tongDiem,x.id))
    print(*a,sep='\n')
