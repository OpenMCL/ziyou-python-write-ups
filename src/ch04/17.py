n = int(input())
num = [[None] * n for i in range(n)]
s, t = 0, 0
s1, t1 = 0, 0
ds, dt = [0, 1, 0, -1], [1, 0, -1, 0]
m = n // 2 + (1 if n % 2 else 0)
dir = 0
for i in range(n * n):
    num[s][t] = i + 1
    if s + t == n - 1 or (s >= m and s == t) or (s < m and s == t + 1):
        dir += 1
        if dir == 4:
            dir = 0
    s += ds[dir]
    t += dt[dir]
print(" " * 2 * (n - 2), end="  ")
for _ in range(n * n):
    print("{:>2}".format(num[s1][t1]), end="  ")
    if s1 == 0 and t1 != n - 1:
        s1 = t1 + 1
        t1 = 0
        print()
        print(" " * 2 * (n - s1 - 1), end="")
    elif t1 == n - 1:
        t1 = s1 + 1
        s1 = n - 1
        print()
        print(" " * 2 * t1, end="")
    else:
        t1 += 1
        s1 -= 1
