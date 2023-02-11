n,m=map(int,input().split())
s1={int (i) for i in input().split()}
s2={int (i) for i in input().split()}
s3=s1.difference(s2)
if len(s3)==0 :
    print('YES')
else:print('NO')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """