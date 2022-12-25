n = int(input("> "))
pca = [[None] * (i + 1) for i in range(n + 1)]
for i in range(n + 1):
    for j in range(i + 1):
        if j == i or j == 0:
            pca[i][j] = 1
        else:
            pca[i][j] = pca[i - 1][j - 1] + pca[i - 1][j]
for i in range(n + 1):
    print(" " * 3 * (n - i), end=" ")
    for j in range(i + 1):
        print("{:>5}".format(pca[i][j]), end=" ")
    print()
for i in range(n - 1, -1, -1):
    print(" " * 3 * (n - i), end=" ")
    for j in range(i + 1):
        print("{:>5}".format(pca[i][j]), end=" ")
    print()
