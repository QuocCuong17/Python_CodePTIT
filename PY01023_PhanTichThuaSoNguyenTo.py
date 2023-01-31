import math
for t in range (int(input())):
    n = int(input())
    res='1'
    for i in range(2,(int)(math.sqrt(n))):
        mu=0
        while(n%i==0):
            mu+=1
            n/=i
        if(mu>0):
            res+=' * ' + str(i)+' ^ '+str(mu)

    if(n!=1):res+=' * '+str(int(n))+' ^ '+'1'
    print(res)