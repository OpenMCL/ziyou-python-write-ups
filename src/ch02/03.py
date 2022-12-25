n1, n2 = int(input("> ")), int(input("> "))
b = len(str(n1 * n2))
nl1 = len(str(n1))
nl2 = len(str(n2))
print(" " * (b - nl1 + 1) + str(n1))
print("x" + " " * (b - nl2) + str(n2))
print("-" * (b + 1))
for i in range(len(str(n2))):
    if n1 * ((n2 % 10 ** (i + 1) - n2 % (10**i))) // (10**i) == 0:
        pass
    else:
        s = len(str((n1 * (n2 % 10 ** (i + 1) - n2 % (10**i)))))
        print(
            " " * (b - s + 1)
            + str((n1 * (n2 % 10 ** (i + 1) - n2 % (10**i))) // (10**i))
        )
print("-" * (b + 1))
print(" " + str(n1 * n2))
