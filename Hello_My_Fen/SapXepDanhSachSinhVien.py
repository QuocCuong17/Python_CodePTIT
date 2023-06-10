class SinhVien:
    def __init__(self,id,name,phone,mail):
        self.id = id
        self.name = name
        self.phone = phone
        self.mail = mail
        res = self.name.split()
        self.fname = res[-1] +self.name
        # print(self.name)
        # print(self.fname)
    def __str__(self):
        return f'{self.id} {self.name} {self.phone} {self.mail}'

if __name__ == '__main__':
    a=[]
    f = open("SINHVIEN.in.txt")
    for __ in range(int(next(f).strip())):
       a.append(SinhVien(next(f).strip(),next(f).strip(),next(f).strip(),next(f).strip()))
    a.sort(key=lambda x:(x.fname,x.id))
    print(*a,sep='\n')
"""
3
B19DCCN999
Ngo Quang Huy
0976555123
B19DCCN999@stu.ptit.edu.vn
B19DCCN998
Nguyen Le Tu
0345678912
B19DCCN998@stu.ptit.edu.vn
B19DCCN997
Nguyen Manh Cuong
0987654321
B19DCCN997@stu.ptit.edu.vn
"""