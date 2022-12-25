n = int(input("> "))
for i in range(-n, n + 1):
    t = "/" if i < 0 else "\\"
    m = "\\" if i < 0 else "/"
    if i == 0:
        continue
    for j in range(-n + 1, n):
        a, b = abs(i), abs(j)
        s = b + 1
        h = s - a + 1
        if a <= s:
            print("|" * (s - h) + t + " " * (h - 1) * 2 + m + "|" * (s - h), end="")
        else:
            print("|" * (s * 2), end="")
    print()
