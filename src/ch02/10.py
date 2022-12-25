n = int(input("> "))
for i in range(-n + 1, n):
    for j in range(-n + 1, n):
        if abs(i - j) <= n - 1 and abs(i + j) <= n - 1:
            print(n - max(abs(i), abs(j)), end=" ")
        else:
            print(" ", end=" ")
    print()
