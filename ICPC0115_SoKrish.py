import math


def kr(n):
    s=0
    m=n
    while n>0 :
        s+=math.factorial(n%10)
        n//=10
    if s==m :return 'Yes'
    return 'No'

if __name__ == '__main__':
    for t in range(int(input())):
        print(kr(int(input())))

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------