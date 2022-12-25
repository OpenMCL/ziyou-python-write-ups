n = int(input("> "))
for i in range(2 * n):
    if i < n:
        print("* " * n + "- " * n * 2)
    else:
        print("+ " * n + "- " * n * 2)
