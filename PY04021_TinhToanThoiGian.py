class NguoiChoi:
    def __init__(self,maNC,tenNC,gioVao,gioRa):
        self.maNC=maNC
        self.tenNC=tenNC
        self.soPhut=60*int(gioRa[0]+gioRa[1])-60*int(gioVao[0]+gioVao[1])+int(gioRa[3]+gioRa[4])-int(gioVao[3]+gioVao[4])
        self.gio=self.soPhut//60
        self.phut=self.soPhut%60
    def __str__(self):
        return self.maNC+" "+self.tenNC+" "+'{:.0f}'.format(self.gio)+" gio "+'{:.0f}'.format(self.phut)+" phut"

if __name__ == '__main__':
    n = int(input())
    a=[]
    for i in range(n):
        nc=NguoiChoi(input(),input(),input(),input())
        a.append(nc)
    a.sort(key=lambda x:-x.soPhut)
    for x in a:
        print(x)
