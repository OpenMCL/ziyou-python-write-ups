n = int(input())
for i in range(-n, n + 1):
    t = "/" if i < 0 else "\\"
    m = "\\" if i < 0 else "/"
    if i == 0:
        continue
    for j in range(-n + 1, n):
        a, b = abs(i), abs(j)
        s = n - b
        h = s - a + 1
        if a <= s and ((i < 0 and (b + n) % 2 == 1) or (i > 0 and (b + n) % 2 == 0)):
            print(" " * (s - h) + t + "|" * (h - 1) * 2 + m + " " * (s - h), end="")
        else:
            print(" " * (s * 2), end="")
    print()
