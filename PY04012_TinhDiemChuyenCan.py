class SinhVien:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade
    def get_score(self,s):
        self.score=res=10-s.count('v')*2-s.count('m')
        self.tt='0 KDDK' if res <=0 else res
    def __str__(self):
        return f'{self.id} {self.name} {self.grade} {self.tt}'

if __name__ == '__main__':
    n = int(input())
    a=[]
    for i in range(n):
        sv = SinhVien(input(),input(),input())
        a.append(sv)
    for i in range(n):
        id,cc=map(str,input().split())
        for i in a:
            if i.id == id:
                i.get_score(cc)
                break
    print(*a,sep='\n')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """