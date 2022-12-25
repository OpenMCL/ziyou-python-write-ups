n = int(input("> "))
dir = [[1, 1], [-1, 0], [0, -1]]
m = [[None for j in range(i + 1)] for i in range(n)]
s, t, c = 0, 0, 0
for i in range(int(n * (n + 1) / 2)):
    m[s][t] = i + 1
    if (
        t + dir[c][0] > s + 1
        or t + dir[c][0] < 0
        or s + dir[c][1] < 0
        or s + dir[c][1] >= n
        or m[s + dir[c][1]][t + dir[c][0]] is not None
    ):
        c = (c + 1) % 3
    t += dir[c][0]
    s += dir[c][1]
for i in range(n):
    for j in range(i + 1):
        print("{:>3}".format(m[i][j]), end=" ")
    print()
