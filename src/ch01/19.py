n = int(input())
for i in range(n):
    for _ in range(n):
        for k in range(i + 1):
            for _ in range(n):
                print(((i * (i + 1)) // 2 + 1 + k) % 10, end=" ")
            print(" ", end="")
        print()
    print()
