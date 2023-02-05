def check(a,b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    for t in range(int(input())):
        t=input()
        a=sorted([int(i) for i in input().split()])
        b=sorted([int(i) for i in input().split()])
        print(check(a,b))