def check(s):
    if(len(s)>=3 and s[-3:]==".py"):
        return 'yes'
    return 'no'
if __name__== '__main__':
    print(check(input().lower()))