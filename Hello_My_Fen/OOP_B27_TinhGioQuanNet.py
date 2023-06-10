from datetime import datetime
class Game:
    def __init__(self,username,password,name,hourin,hourout):
        self.username = username
        self.password = password
        self.name = name
        self.hourout = hourout
        self.hourin = hourin
        self.second = (datetime.strptime(hourout,"%H:%M") - datetime.strptime(hourin,"%H:%M")).seconds
        self.hour = self.second//3600
        self.minute = self.second%60
    def __str__(self):
        return f'{self.username} {self.password} {self.name} {self.hour} gio {self.minute} phut'
if __name__ == "_main__":
    a = []
    n = int(input())
    for i in range(n):
        a.append(Game(input(),input(),input(),input(),input()))
    a.sort(key=lambda x:(-x.second,x.username))
    print(*a,sep="\n")
