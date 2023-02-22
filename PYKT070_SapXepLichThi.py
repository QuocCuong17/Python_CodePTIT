from datetime import datetime
class MonThi:
    def __init__(self,id,name,ht):
        self.id=id
        self.name=name
        self.ht=ht
    def __str__(self):
        return self.name
class CaThi:
    def __init__(self,id,date,hour,phong):
        self.date=date
        self.hour=hour
        self.phong=phong
        self.id = 'C'+format(id,'03d')
    def __str__(self):
        return f'{self.date} {self.hour} {self.phong}'
class LichThi:
    def __init__(self,idct,idmon,idnhom,sl):
        self.idct=idct
        self.idmon=idmon
        self.idnhom=idnhom
        self.sl=sl
    def __str__(self):
        return f'{self.idct} {self.idmon} {self.idnhom} {self.sl}'
if __name__ == '__main__':
    monthi,cathi,lichthi=[],[],[]
    mt,ct,lt=open('MONTHI.in','r'),open('CATHI.in','r'),open('LICHTHI.in','r')
    n1 = int(next(mt).strip())
    for i in range(n1):
        m=MonThi(next(mt).strip(),next(mt).strip(),next(mt).strip())
        monthi.append(m)
    n2= int(next(ct).strip())
    for i in range(n2):
        c=CaThi(i+1,next(ct).strip(),next(ct).strip(),next(ct).strip())
        cathi.append(c)
    n3 = int(next(lt).strip())
    for i in range(n3):
        s=next(lt).strip().split()
        idct=s[0]
        idmon=s[1]
        idnhom=s[2]
        sl=s[3]
        mon,ca='',''
        for j in monthi:
            if j.id==idmon:
                mon=j
                break
        for j in cathi:
            if j.id==idct:
                ca=j
                break
        l=LichThi(ca,mon,idnhom,sl)
        lichthi.append(l)
    lichthi=sorted(lichthi,key=lambda x:(datetime.strptime(x.idct.date,'%d/%m/%Y'),datetime.strptime(x.idct.hour,'%H:%M'),x.idct.id))
    print(*lichthi,sep="\n")
"""
Input:
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
2
09/01/2022
15:30
70172
09/01/2022
10:00
70279
2
C001 MUL1320 01 46
C002 BAS1203 04 72

Output:
09/01/2022 10:00 Giai tich 1 04 72
09/01/2022 15:30 Nhap mon da phuong tien 01 46
"""

"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """