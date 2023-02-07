if __name__ == '__main__':
    cnt1={}
    cnt2={}
    cnt3={}
    a = [i.lower() for i in input().split(' ')]
    b = [i.lower() for i in input().split(' ')]
    for i in a:
        cnt1[i]=1
        cnt2[i]=1
    for i in b:
        cnt1[i]=1
        cnt3[i]=1
    for i in sorted(list(cnt1)):
        print(i,end=' ')
    print()
    for i in sorted(list(cnt2)):
        if i in cnt3:
            print(i,end=' ')

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------