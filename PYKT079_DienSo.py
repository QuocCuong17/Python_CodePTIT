for t in range(int(input())):
    n = int(input())
    a= {int(i) for i in input().split()}
    max_val=max(a)
    min_val=min(a)
    ans=max_val-min_val+1
    if (ans==len(a)):
        print(0)
    else:
        print(ans-len(a))