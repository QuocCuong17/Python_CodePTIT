if __name__ == '__main__':
    dem = 0
    m = [0] * 42
    while True:
        a = [int(i) for i in input().split()]
        cnt = 0
        dem += len(a)

        for i in a:
            m[i % 42] = 1
        if dem % 10 == 0: break
    for i in m:
        if i > 0:
            cnt+=1
    print(cnt)
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """