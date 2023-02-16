import math


class PhanSo:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def toigian(self):
        ucln=math.gcd(self.x,self.y)
        self.x//=ucln
        self.y//=ucln
    def __str__(self):
        return f'{self.x}/{self.y}'
if __name__ == '__main__':
    a=input().split()
    p = PhanSo(int(a[0]),int(a[1]))
    p.toigian()
    print(p)