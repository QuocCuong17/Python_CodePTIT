if __name__ == '__main__':
    s=input()
    m={}
    a=[int(i) for i in input().split()]
    for i in range(1,30001):
        if not i in a:
            print(i)
            break
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """