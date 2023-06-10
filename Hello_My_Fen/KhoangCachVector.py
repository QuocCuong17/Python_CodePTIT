import math


def euclidean(v1,v2):
    kc = math.sqrt(sum((x-y)**2 for x,y in zip(v1,v2)))
    return "{:.5f}".format(kc)
def manhattan(v1,v2):
    kc = sum(abs(x-y) for x,y in zip(v1,v2))
    return "{:.5f}".format(kc)
def minkowski(v1,v2):
    p = 3
    kc = (sum(abs((x-y)**p) for x,y in zip(v1,v2)))
    return "{:.5f}".format(kc)
def jaccard(v1,v2):
    v1 = set(v1)
    v2 = set(v2)
    kc = len(v1.intersection(v2)) / len(v1.union(v2))
    return "{:.5f}".format(kc)
if __name__ == "__main__":
    for __ in range(int(input())):
        s = input()
        v1 = list(map(int,input().split()))
        v2 = list(map(int, input().split()))
        if len(v1) != len(v2):
            print("Invalid")
        if s == "euclidean":
            print(euclidean(v1, v2))
        elif s == "manhattan":
            print(manhattan(v1,v2))
        elif s == "minkowski":
            print(minkowski(v1,v2))
        elif s == "jaccard":
            print(jaccard(v1,v2))
"""
4
euclidean
1 4
0 0
manhattan
2 4 6
2 0 
minkowski
1 4
0 0
jaccard
1 4
0 0
"""

"""              -------            --------              ---------
                -        -        -          -          -
                -         -      -            -        -
               ----       -      -            -        -
                -         -      -         -  -        -
                -        -        -          -          -
                --------            --------   -          ---------         """
