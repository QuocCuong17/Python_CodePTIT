from _datetime import datetime
class CaThi:
    def __init__(self,id,date,hour,idp):
        self.id ='C'+format(id,'03d')
        self.date=date
        self.hour=hour
        self.idp=idp
    def __str__(self):
        return f'{self.id} {self.date} {self.hour} {self.idp}'
if __name__ == '__main__':
    f=open('CATHI.in','r')
    ct=[]
    n=int(next(f).strip())
    for i in range(n):
        c = CaThi(i+1,next(f).strip(),next(f).strip(),next(f).strip())
        ct.append(c)
    ct=sorted(ct,key=lambda x:(datetime.strptime(x.date,'%d/%m/%Y'),datetime.strptime(x.hour,'%H:%M'),x.id))
    print(*ct,sep='\n')

