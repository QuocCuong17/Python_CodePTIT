class MonThi:
    def __init__(self,id,name,form):
        self.id=id
        self.name=name
        self.form=form
    def __str__(self):
        return f'{self.id} {self.name} {self.form}'
if __name__ == "__main__":
    n=int(input())
    a=[]
    for i in range(n):
        mh=MonThi(input(),input(),input())
        a.append(mh)
    a.sort(key=lambda x:x.id)
    print(*a,sep='\n')
