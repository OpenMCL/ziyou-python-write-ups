import random

count = [0 for i in range(6)]
for i in range(2, 8):
    for _ in range(pow(6, i)):
        r = [random.randint(1, 6) for j in range(i)]
        s = [r.count(j) for j in range(1, 7)]
        if sum([j > 2 for j in s]) == 0 and s.count(2) == 1:
            count[i - 2] += 1
for i in range(6):
    print("{:>6}".format(i + 2), end=" ")
print()
for i in range(6):
    print("=" * 6, end="=")
print()
for i in range(6):
    print("{:>6}".format(count[i]), end=" ")
print()
for i in range(6):
    print("{:>6}".format("-" * len(str(pow(6, i + 2)))), end=" ")
print()
for i in range(6):
    print("{:>6}".format(pow(6, i + 2)), end=" ")
