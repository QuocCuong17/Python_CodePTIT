from datetime import datetime
class LuongMua:
    def __init__(self,id,ten,start,end,lmua):
        self.id = 'T'+format(id,'02d')
        self.ten = ten
        self.time = datetime.strptime(end,'%H:%M') - datetime.strptime(start,'%H:%M')
        self.lmua = lmua
    def __str__(self):
        return '{:s} {:s} {:.2f}'.format(self.id,self.ten,self.lmua*3600/self.time.seconds)
l = []
def inList(s):
    for i in l:
        if i.ten == s.ten:
            i.lmua += s.lmua
            i.time += s.time
            return
    l.append(s)

if __name__ == "__main__":
    for t in range(int(input())):
        data = LuongMua(t+1, input(), input(), input(), int(input()))
        inList(data)
    print(*l, sep='\n')
