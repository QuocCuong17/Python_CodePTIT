class ThiSinh:
    def __init__(self,name,dob,d1,d2,d3):
        self.name=name
        self.dob=dob
        self.tong=d1+d2+d3
    def __str__(self):
        return self.name+" "+self.dob+" "+'{:.1f}'.format(self.tong)
if __name__ == '__main__':
    name=input()
    dob=input()
    d1=float(input())
    d2=float(input())
    d3=float(input())
    t = ThiSinh(name,dob, d1, d2, d3)
    print(t)