n = int(input())
for i in range(-n + 1, n):
    for k in range(2):
        for w in range(2):
            for j in range(-n + 1 if w == 0 else -n + 2, n):
                a, b = abs(i), abs(j)
                if a <= b:
                    print("\\|/" if k == 0 else "/|\\", end=" ")
                else:
                    print("   ", end=" ")
        print()
