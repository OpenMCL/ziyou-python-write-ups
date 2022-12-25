n = int(input("> "))
# -1 = \ ; -2 = / ; -3 = *
photo = [[0] * (2 * n + 1) for i in range(2 * n + 3)]
mid = n + 1
for i in range(0, n, 1):
    photo[mid][i * 2] = n - i
    for j in range(1, n - i + 2):
        photo[mid + j][i * 2 + j] = -1
        photo[mid - j][i * 2 + j] = -2
        if j == n - i + 1:
            photo[mid + j][i * 2 + j] = -3
            photo[mid - j][i * 2 + j] = -3

for i in range(2 * n + 3):
    for j in range(2 * n + 1):
        if photo[i][j] == 0:
            print(" ", end="")
        elif photo[i][j] == -1:
            print("\\", end="")
        elif photo[i][j] == -2:
            print("/", end="")
        elif photo[i][j] == -3:
            print("*", end="")
        else:
            print(photo[i][j], end="")
    print()
