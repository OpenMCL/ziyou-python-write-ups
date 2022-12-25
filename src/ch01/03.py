n = int(input("> "))
c = 1
for _ in range(n):
    for _ in range(n):
        print(c % 10, end=" ")
        c += 1
    print()
