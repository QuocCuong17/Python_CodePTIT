class SoTay:
    def __init__(self,date,name,phone):
        self.date = date
        self.name = name
        self.phone = phone
    def get_ten(self):
        res=''
        res=self.name[-1]
        res+=self.name
        return res
    def __str__(self):
        return f'{self.name}: {self.phone} {self.date}'
if __name__ == "__main__":
    ngay=''
    a=[]
    f = open("SOTAY.txt",'r')
    try:
        while True:
            s = next(f).strip()
            if s.startswith("Ngay"):
                ngay=s[5:]
            else:
                a.append(SoTay(ngay,s,next(f).strip()))
    except StopIteration: f.close()
    a=sorted(a,key=lambda x:x.get_ten())
    dt = open("DIENTHOAI.txt",'w')
    dt.write("\n".join([str(i) for i in a]))
    dt.close()