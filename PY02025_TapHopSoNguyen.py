a,b=map(int,input().split())
s1={int (i) for i in input().split()}
s2={int (i) for i in input().split()}
s3=s1.intersection(s2)
s3=sorted(s3)
s4=s1-s2
s4=sorted(s4)
s5=s2-s1
s5=sorted(s5)
for i in s3:
    print(i,end=' ')
print()
for i in s4:
    print(i, end=' ')
print()
for i in s5:
    print(i, end=' ')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """