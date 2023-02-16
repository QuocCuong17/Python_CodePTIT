class VanToc:
    def __init__(self,hoTen,donVi,timeFn):
        self.hoTen=hoTen
        self.donVi=donVi
        self.timeFn=timeFn
        soPhut = 60*int(timeFn[0] ) - 6 * 60 + int(timeFn[2] + timeFn[3])
        soGio = soPhut / 60
        self.speed=120/soGio
    def get_ma(self):
        res=''
        for i in self.donVi.split():
            res+=i[0]
        for i in self.hoTen.split():
            res+=i[0]
        return res
    def __str__(self):
        return self.get_ma()+" "+self.hoTen+" "+self.donVi+" "+'{:.0f}'.format(self.speed)+" Km/h"
if __name__ == '__main__':
    a=[]
    n = int(input())
    for i in range(n):
        vt = VanToc(input(),input(),input())
        a.append(vt)
    a.sort(key=lambda x:-x.speed)
    for x in a:
        print(x)
