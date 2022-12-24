import random

n = int(input())
ans = str(random.randint(1000, 9999))
print("  ", ans)

for i in range(n):
    a, b = 0, 0
    r = str(random.randint(1000, 9999))
    print("{:>2} {} : ".format(i + 1, r), end="")
    for j in r:
        if j in ans:
            if r.index(j) == ans.index(j):
                a += 1
            else:
                b += 1
    print("{}A{}B".format(a, b))
