if __name__ == '__main__':
    while True:
        n=int(input())
        if n ==0:
            break
        cnt=1
        while(n!=1):
            cnt+=1
            if(n%2==0):
                n=n/2
            else:n=n*3+1
        print(cnt)
"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """