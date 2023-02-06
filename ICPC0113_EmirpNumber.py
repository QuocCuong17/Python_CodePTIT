import math


def snt(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i==0 : return False
    return True


if __name__ == '__main__':
    for t in range(int(input())):
        n=int(input())
        for i in range(2,n):
            k=int(str(i)[::-1])
            if k>i and k<n and snt(int(i)) and snt(k):
                print(i,k,end=' ')
        print()

#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------