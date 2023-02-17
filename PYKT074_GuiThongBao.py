if __name__ == '__main__':
    for t in range(int(input())):
        a=[i for i in input().split()]
        dem=0
        for i in a:
            if dem+len(i)>100: break
            print(i,end='')
            dem+=len(i)
            print(end=' ')
            dem+=1
        print()
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """