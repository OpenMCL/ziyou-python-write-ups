n = int(input())
for i in range(3):
    for _ in range(n):
        for k in range(3):
            if i == k:
                for _ in range(n):
                    print(i + k + 1, end="")
            elif abs(i - k) == 2:
                for _ in range(n):
                    print(i * 2 + k, end="")
            else:
                for _ in range(n):
                    print(" ", end="")
        print()
