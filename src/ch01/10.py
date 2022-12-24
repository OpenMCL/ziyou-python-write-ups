n = int(input())
for i in range(n):
    print("|", end="")
    for j in range(n):
        for k in range(n):
            print((i + j + k) % n + 1, end="")
        print("|", end="")
    print()
