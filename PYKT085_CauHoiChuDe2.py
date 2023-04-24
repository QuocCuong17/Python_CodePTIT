a=[]
for i in range(int(input())):
    s= input()
    if s=='':
        print(a[0],": ",len(a)-1,sep='',end='\n')
        a.clear()
    else:a+=[s]
print(a[0],": ",len(a)-1,sep='',end='\n')   
"""
9
Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?

Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?
"""