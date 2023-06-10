from datetime import datetime
class PTIT:
    def __init__(self,name,st,en):
        self.name = name
        self.st = st
        self.en = en
        self.min = (datetime.strptime(self.en,"%d/%m/%Y %H:%M:%S")-datetime.strptime(self.st,"%d/%m/%Y %H:%M:%S")).seconds//60 \
                   + (datetime.strptime(self.en,"%d/%m/%Y %H:%M:%S")-datetime.strptime(self.st,"%d/%m/%Y %H:%M:%S")).days*24*60

    def __str__(self):
        return f'{self.name} {self.min}'

if __name__ == '__main__':
    a=[]
    f = open("ONLINE.in",'r')
    n = int(f.readline().strip())
    for __ in range(n):
        a.append(PTIT(next(f).strip(),next(f).strip(),next(f).strip()))
    a.sort(key=lambda x:(-x.min,x.name))
    print(*a,sep='\n')

"""
3
Do Viet Anh
11/12/2021 16:35:00
11/12/2021 17:35:00
Le Tuan Anh
11/12/2021 16:45:00
11/12/2021 18:15:00
Nguyen Tuan Anh
11/12/2021 17:00:00
11/12/2021 19:15:00
"""