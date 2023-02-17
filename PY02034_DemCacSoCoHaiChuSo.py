import re
if __name__ == '__main__':
    s=input()
    r='\d\d'
    m={}
    a=re.findall(r,s)
    for i in a:
        if i in m:
            m[i]+=1
        else:m[i]=1
    for i,j in m.items():
        print(i,' ',j)
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """