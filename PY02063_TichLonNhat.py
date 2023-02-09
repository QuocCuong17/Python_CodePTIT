if __name__ == '__main__':
    s = input()
    a = [int(i) for i in input().split()]
    a = sorted(a)
    max1=a[0]*a[1]
    max2=a[-1]*a[-2]
    max3=a[0]*a[1]*a[-1]
    max4=a[-1]*a[-2]*a[-3]
    print(max(max1,max2,max3,max4))