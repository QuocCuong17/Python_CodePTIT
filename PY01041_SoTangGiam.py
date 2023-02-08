def check(s):
    if len(s) < 3: return 'NO'
    if s[1] <= s[0] or s[-1] >= s[-2]: return 'NO'
    l = 1
    r = len(s)-2
    while s[l] > s[l-1] and l < len(s):
        l+=1
    while s[r] > s[r+1] and r >= 0:
        r-=1
    if l == r+2 :
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
     for t in range(int(input())):
        print(check(input()))
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """