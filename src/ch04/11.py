n = int(input())
for i in range(n, 6 * n + 1):
    print(f"{i:n}", end=" ")
print()
print("=== " * (5 * n + 1))


def dice(n):
    if n == 1:
        return [1 for i in range(6)]
    else:
        m = []
        ld = dice(n - 1)
        for i in range(5 * n + 1):
            if i <= 5 * (n - 1):
                m.append(ld[i])
            else:
                m.append(0)
        p = [0 for i in range(5 * n + 1)]
        for i in range(5 * n + 1):
            if i < 6:
                p[i] = sum(m[0 : i + 1 : 1])
            else:
                p[i] = sum(m[i : i - 6 : -1])
        return p


for i in dice(n):
    print("{:>3}".format(i), end=" ")
print()
print("--- " * (5 * n + 1))
for i in range(5 * n + 1):
    print("{:>3}".format(6**n), end=" ")
