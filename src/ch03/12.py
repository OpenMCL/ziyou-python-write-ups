n = int(input())

for i in range(1, n + 1):
    for j in range(3):
        for k in range(1, n + 1):
            if i == k or k == n - i + 1:
                print(str(n) * 3, end="")
            else:
                print("   ", end="")
        print()
