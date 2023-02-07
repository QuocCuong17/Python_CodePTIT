for t in range(int(input())):
    print("Test ",(t+1),': ',sep="",end="")
    s1=sorted(input())
    s2=sorted(input())
    if s1==s2:
        print('YES')
    else:print('NO')

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------