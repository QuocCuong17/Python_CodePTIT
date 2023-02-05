if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        a=[]
        sum_digit=0
        for i in s:
            if i.isdigit():
                sum_digit+=int(i)
            else:a.append(i)
        a=sorted(a)
        for i in a:
            print(i,end='')
        print(sum_digit)