import math
for t in range (int(input())):
    s=input()
    if(math.gcd((int)(s),(int)(s[::-1])) == 1):
        print("YES")
    else: print("NO")