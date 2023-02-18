from itertools import combinations
if __name__ == '__main__':
    n,k=map(int,input().split())
    se={str(i) for i in input().split()}
    se= sorted(se)
    for i in list(combinations(se,k)):
        print(*i)