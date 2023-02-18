if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        a.insert(a.index(max(a)), m)
        b, c = [], []
        for x in a:
            if x >= 0:
                b.append(x)
            else:
                c.append(x)
        print(*c, end=' ')
        print(*b, sep=' ', end='\n')
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """