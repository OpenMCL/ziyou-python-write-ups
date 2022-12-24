from random import randint

n = int(input())
# set matrix size
m1 = [[0 for j in range(n)] for i in range(n)]
m2 = [[0 for j in range(n)] for i in range(n)]
ans = [[0 for j in range(n)] for i in range(n)]
# produce matrices
for i in range(n):
    for j in range(i + 1):
        m1[i][j] = randint(0, 1)
        m1[j][i] = m1[i][j]
        m2[i][j] = randint(0, 1)
        m2[j][i] = m2[i][j]
# compute matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += m1[i][k] * m2[k][j]
# output
for i in range(n):
    for j in range(n):
        print(m1[i][j], end="  ")
    if i == n // 2:
        print("x", end="  ")
    else:
        print(" ", end="  ")
    for j in range(n):
        print(m2[i][j], end="  ")
    if i == n // 2:
        print("=", end="  ")
    else:
        print(" ", end="  ")
    for j in range(n):
        print(ans[i][j], end="  ")
    print()
