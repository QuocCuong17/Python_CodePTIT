import math


class PhanSo:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def toigian(self):
        ucln=math.gcd(self.x,self.y)
        self.x//=ucln
        self.y//=ucln
    def add(self,other):
        return PhanSo(self.x*other.y+self.y*other.x,self.y*other.y)
    def __str__(self):
        return f'{self.x}/{self.y}'
if __name__ == '__main__':
    a=input().split()
    p1 = PhanSo(int(a[0]),int(a[1]))
    p2 = PhanSo(int(a[2]),int(a[3]))
    p3 = p1.add(p2)
    p3.toigian()
    print(p3)