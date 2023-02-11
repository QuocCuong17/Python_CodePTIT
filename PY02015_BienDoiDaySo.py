if __name__ == '__main__':
    while True:
        a=[int(i) for i in input().split()]
        if a == [0, 0, 0, 0]: break
        cnt=0
        for i in range(0,1000000):
            if a[0]==a[1] and a[1]==a[2] and a[2]==a[3]:
                print(i)
                break
            tmp = a[0]
            a[0] = abs(a[0]-a[1])
            a[1] = abs(a[1]-a[2])
            a[2] = abs(a[2] - a[3])
            a[3] = abs(a[3]-tmp)
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """