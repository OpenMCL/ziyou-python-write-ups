n = int(input())
a = [[None for _ in range(j + 1)] for j in range(n)]
s, t = 0, 0
for i in range(int((1 + n) * n / 2)):
    a[s][t] = i + 1
    if not s % 2:
        if s == t:
            s += 1
        t += 1
    else:
        if t == 0:
            s += 1
        else:
            t -= 1
for i in range(n):
    for j in range(i + 1):
        print("{:>3}".format(a[i][j]), end=" ")
    print()
