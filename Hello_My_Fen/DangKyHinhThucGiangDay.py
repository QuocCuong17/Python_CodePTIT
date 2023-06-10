class MonHoc:
    def __init__(self,id,name,soTC,LT,TH):
        self.id = id
        self.name = name
        self.soTC = soTC
        self.LT = LT
        self.TH = TH
    def __str__(self):
        return f'{self.id} {self.name} {self.soTC} {self.LT} {self.TH}'

if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        a.append(MonHoc(input(),input(),int(input()),input(),input()))
    a.sort(key=lambda x:x.id)
    print(*a,sep="\n")