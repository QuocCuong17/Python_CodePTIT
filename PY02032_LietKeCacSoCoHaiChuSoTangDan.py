import re
if __name__ == '__main__':
    s=input()
    r='\d\d'
    m={}
    a=re.findall(r,s)
    se=sorted({x for x in a})
    for x in se:
        print(x,end=' ')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """