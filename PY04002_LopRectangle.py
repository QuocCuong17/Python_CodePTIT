class Rectangle:
    def __init__(self,x,y,cl):
        self.x=x
        self.y=y
        self.cl=cl
    def chuVi(self):
        return (self.x+self.y)*2
    def dienTich(self):
        return self.x*self.y
    def mauSac(self):
        return self.cl.title()
try:
    if __name__ == '__main__':
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
except:

    if int(arr[0]) <=0  or int(arr[1])<=0:
        print('INVALID')
    else:
        r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
        print('{} {} {}'.format(r.chuVi(), r.dienTich(), r.mauSac()))