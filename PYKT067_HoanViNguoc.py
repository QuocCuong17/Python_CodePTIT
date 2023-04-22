import itertools
from itertools import permutations
if __name__ == "__main__":
    test = int(input())
    for t in range(test):
        n = int(input())
        a=list(itertools.permutations(range(1,n+1)))
        print(len(a))
        for i in a[::-1]:
            print(*i,sep='',end=' ')
        print()