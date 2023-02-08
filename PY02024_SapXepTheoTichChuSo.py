def mtp(n):
    m=1
    for i in n:
        m*=int(i)
    return m

if __name__ == '__main__':
    for t in  range(int(input())):
        s=input()
        l=input().split()
        l.sort(key=lambda s:(mtp(s),int(s)))
        print(*l)

"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """
