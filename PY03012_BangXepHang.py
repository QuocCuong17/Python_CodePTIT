class SinhVien:
    def __init__(self,name,c,t):
        self.name=name
        self.c=c
        self.t=t
    def __str__(self):
        return f'{self.name} {self.c} {self.t}'
if __name__ == '__main__':
    a=[]
    n=int(input())
    for i in range(n):
        name=input()
        s=input().split()
        sv = SinhVien(name,int(s[0]),int(s[1]))
        a.append(sv)
    a.sort(key=lambda x:(-x.c,x.t,x.name))
    print(*a,sep='\n')
