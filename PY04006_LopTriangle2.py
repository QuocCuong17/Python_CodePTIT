import math


class Point:
    def __init__(self,p):
        self.x=p[0]
        self.y=p[1]
    def khoangCach(self,o):
        return math.sqrt((self.x-o.x)*(self.x-o.x)+(self.y-o.y)*(self.y-o.y))
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        x = self.a.khoangCach(self.b)
        y = self.a.khoangCach(self.c)
        z = self.b.khoangCach(self.c)
        return 'INVALID' if max(x,y,z) * 2 >= x+y+z else '{:.2f}'.format(math.sqrt((x+y+z)*(x+y-z)*(-x+y+z)*(x-y+z))/4)

if __name__=='__main__':
    a=[]
    t=int(input())
    i=0
    for __ in range(t):
        a += [float(i) for i in input().split()]
    for __ in range(t):
        print(Triangle(Point(a[i:i + 2]), Point(a[i + 2:i + 4]), Point(a[i + 4:i + 6])))
        i += 6