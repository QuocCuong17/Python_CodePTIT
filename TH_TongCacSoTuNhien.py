def init():
    n = int(input())
    k = 1
    count = 0
    C = [0] * MAX
    C[k] = n
    Stop = False
    return n, k, count, C, Stop


def result(count, C, k, ls_res):
    count += 1
    res = "("
    for i in range(1, k + 1):
        res += str(C[i]) + " "
    res = res[:-1] + ")"
    ls_res.append(res)
    return count


def next_division(k, C):
    i = k
    while i > 0 and C[i] == 1:
        i -= 1
    if i > 0:
        C[i] -= 1
        D = k - i + 1
        R = D // C[i]
        S = D % C[i]
        k = i
        if R > 0:
            for j in range(i + 1, i + R + 1):
                C[j] = C[i]
            k += R
        if S > 0:
            k += 1
            C[k] = S
        Stop = False
    else:
        Stop = True
    return k, C, Stop


def division(n, k, count, C, Stop, ls_res):
    while not Stop:
        count = result(count, C, k, ls_res)
        k, C, Stop = next_division(k, C)


for _ in range(int(input())):
    MAX = 100
    n, k, count, C, Stop = init()
    ls_res = []
    division(n, k, count, C, Stop, ls_res)
    print(len(ls_res))
    print(*ls_res)