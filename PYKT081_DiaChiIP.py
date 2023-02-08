def checkip(s):
    if len(s) != 4:
        return 'NO'
    for i in s:
        if i.isdigit():
            if int(i)>255 or int(i)<0:
                return 'NO'
        else:return 'NO'
    return 'YES'
if __name__ == '__main__':
    for t in range (int(input())):
        print(checkip(input().split('.')))
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """