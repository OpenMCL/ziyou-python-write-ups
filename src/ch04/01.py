n = int(input())
s = [[0 for j in range(n * 2 - 1)] for i in range(n * 2 - 1)]
for i in range(len(s)):
    for j in range(len(s[0])):
        k, m = i - n + 1, j - n + 1
        s[i][j] = max(abs(k) + 1, abs(m) + 1)

for i in range(len(s)):
    for j in range(len(s[0])):
        k, m = i - n + 1, j - n + 1
        if (
            (k > m and k < 0)
            or (k < m and k > 0)
            or (abs(k) > m and m > 0 and k < 0)
            or ((k) > abs(m) and m < 0 and k > 0)
        ):
            print(" ", end=" ")
        else:
            print(s[i][j], end=" ")
    print()
