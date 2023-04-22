class ThiSinh:
    def __init__(self,id,name,diem,danToc,khuVuc):
        self.id = "TS"+format(id, "02d")
        self.name = name
        self.diem =diem
        self.danToc = danToc
        self.khuVuc= khuVuc
    def chuan_hoa(self):
        tmp=self.name.split()
        res=" ".join(tmp)
        self.name=res.title()
    def get_tong_diem(self):
        res = self.diem
        if self.khuVuc=='1':
            res+=1.5
        elif self.khuVuc=='2':
            res+=1
        if self.danToc=="Kinh":
            res +=0
        else:res+=1.5
        return res
    def get_tt(self):
        if self.get_tong_diem()>=20.5:
            return "Do"
        else:return "Truot"
    def __str__(self):
        return '{:s} {:s} {:.1f} {:s}'.format(self.id,self.name,self.get_tong_diem(),self.get_tt())
if __name__ == "__main__":
    t=[]
    n = int(input())
    for i in range(n):
       s = ThiSinh(i+1,input(),float(input()),input(),input())
       s.chuan_hoa()
       t.append(s)
    t = sorted(t, key=lambda x: (-x.get_tong_diem(),x.id))
    print(*t,sep='\n')


