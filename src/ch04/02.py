n = int(input())
for i in range(n):
    for j in range(n):
        k = j - i
        print(abs(k) + 1, end="  ")
    print()
