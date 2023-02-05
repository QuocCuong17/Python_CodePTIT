f=[1]*93
for i in range(3,93):
    f[i]=f[i-1]+f[i-2]
if __name__ == '__main__':
    for t in range(int(input())):
        a,b = map(int,input().split())
        for i in range(a,b+1):
            print(f[i],end=" ")
        print()