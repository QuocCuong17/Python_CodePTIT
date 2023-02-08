def RC(s):
    if   s<4:   return 2.50
    elif s<7: return 3.00
    elif s<10: return 3.50
    elif s<13: return 4.00
    elif s<16: return 4.50
    elif s<20: return 5.00
    elif s<23: return  5.50
    elif s<27: return 6.00
    elif s<30: return 6.50
    elif s<33: return 7.00
    elif s<35: return 7.50
    elif s<37: return 8.00
    elif s<39: return 8.50
    else     : return 9.00

if __name__ == '__main__':
    for t in range(int(input())):
        r,l,s,w = map(float,input().split())
        r=RC(r)
        l=RC(l)
        avg = (r+l+s+w)/4.0
        s = str(avg)
        if avg - int(avg) >= 0.75:
            print(int(avg) + 1.0)
        elif avg - int(avg) >= 0.25:
            print(int(avg) + 0.5)
        else:
            print(int(avg))
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """