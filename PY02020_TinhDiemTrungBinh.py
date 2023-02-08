n = int(input())
a=([float(i) for i in input().split()])
a=sorted(a)
list=[]
maxx=max(a)
minn=min(a)
for i in a:
    if i!=maxx and i!=minn:
        list.append(i)
print("{:.2f}".format(sum(list)/len(list)))
#                --------            --------             ---------
#                -        -        -          -          -
#                -         -      -            -        -
#               ----       -      -            -        -
#                -         -      -         -  -        -
#                -        -        -          -          -
#                --------            --------   -          ---------