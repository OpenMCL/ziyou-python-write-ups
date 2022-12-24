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
        if a == s:
            print((str(s)) * s, end="")
        elif a < s:
            print("-" * s, end="")
        else:
            print(" " * (s), end="")
    print()
