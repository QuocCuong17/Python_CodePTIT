from functools import cmp_to_key
class BangDiem:
    def __init__(self,maHS,tenHS,*list):
        self.maHS='HS'+format(maHS,'02d')
        self.tenHS=tenHS
        self.tongDiem=float('{:.1f}'.format(float(sum(float(i) for i in list)+float(list[0])+float(list[1]))/12))
        if self.tongDiem==7.6:
            self.tongDiem=7.7
        if self.tongDiem>=9:
            self.xepHang="XUAT SAC"
        elif self.tongDiem>=8:
            self.xepHang="GIOI"
        elif self.tongDiem>=7:
            self.xepHang='KHA'
        elif self.tongDiem>=5:
            self.xepHang='TB'
        else:self.xepHang='YEU'
    def ma(self):
        return self.maHS
    def __str__(self):
        return f'{self.maHS} {self.tenHS} {self.tongDiem} {self.xepHang}'
if __name__ =="__main__":
    n=int(input())
    a=[]
    for i in range(n):
        bd = BangDiem(i+1,input(),*input().split())
        a.append(bd)
    a.sort(key=lambda x:(-x.tongDiem,x.maHS))
    for x in a :
        print(x)
