if __name__ == '__main__':
    while True:
        n=int(input())
        if n==0: break
        a=[1]*n
        for i in range(n):
            a[i]=int(input())
        minn = min(a)
        maxx = max(a)
        if minn == maxx :
            print("BANG NHAU")
        else:
            print(minn,maxx,sep=' ')
            print()
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """