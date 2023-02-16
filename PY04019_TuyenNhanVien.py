class NhanVien:
    def __init__(self,maTS,tenTS,diemLT,diemTH):
        self.maTS='TS0'+str(maTS)
        while diemLT>10:
            diemLT/=10
        while diemTH>10:
            diemTH/=10
        self.tenTS=tenTS
        self.avg=(diemTH+diemLT)/2
    def xep_hang(self):
        if (self.avg>9.5):
            return "XUAT SAC"
        elif(self.avg>=8):
            return "DAT"
        elif(self.avg>=5):
            return "CAN NHAC"
        else: return "TRUOT"
    def __str__(self):
        return self.maTS+"  "+self.tenTS+" "+ '{:.2f}'.format(self.avg)+" "+self.xep_hang()
if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(n):
        nv = NhanVien(i+1,input(),float(input()),float(input()))
        a.append(nv)
    a.sort(key=lambda x:-x.avg)
    for x in a:
        print(x)
