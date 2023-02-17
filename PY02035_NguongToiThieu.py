import re
if __name__ == '__main__':
    s = input()
    k = int(input())
    r = '\d\d'
    lst = re.findall(r, s)
    m = {}
    for i in lst:
        if i in m:
            m[i] += 1
        else:
            m[i] = 1
    ok = 0
    for i in sorted(m):
        if (m[i]) >= k:
            print(i, ' ', m[i])
            ok = 1
    if ok == 0:
        print("NOT FOUND")
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """