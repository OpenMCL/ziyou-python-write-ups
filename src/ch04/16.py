n = input("> ")
for i in range(int(max(n)) - 1, -1, -1):
    for j in range(len(n)):
        if n[j] == "0":
            continue
        if i < int(n[j]):
            print(pow(10, len(n) - j - 1), end=" ")
        else:
            print(" " * (len(n) - j), end=" ")
    print()
