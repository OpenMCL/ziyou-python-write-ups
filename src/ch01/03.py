n = int(input())
c = 1
for i in range(n):
    for j in range(n):
        print(c % 10, end=" ")
        c += 1
    print()
