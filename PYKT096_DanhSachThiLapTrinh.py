class Team:
    def __init__(self,id,tname,sname):
        self.id = 'Team'+format(id,'02d')
        self.tname=tname
        self.sname=sname
    def __str__(self):
        return f'{self.tname} {self.sname}'
class Candidate:
    def __init__(self,id,name,idt):
        self.id ='C'+format(id,'03d')
        self.name =name
        self.idt=idt
    def __str__(self):
        return f'{self.id} {self.name} {self.idt}'
if __name__ == '__main__':
    t,c=[],[]
    n=int(input())
    for i in range(n):
        b=Team(i+1,input(),input())
        t.append(b)
    m=int(input())
    for i in range(m):
        a=input()
        b=input()
        for j in (t):
            if j.id == b:
                cdd=Candidate(i+1,a,j)
                c.append(cdd)
    c.sort(key=lambda x:x.name)
    print(*c,sep='\n')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """