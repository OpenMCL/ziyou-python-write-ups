n = int(input())
ans = [[0 for _ in range(n)] for _ in range(n)]

count = 1
for i in range(n):
    for j in range(i, n):
        ans[j][i] = count
        count += 1
for i in ans:
    for j in i:
        if j == 0:
            print(end=" ")
        else:
            print("{:>2}".format(j), end=" ")
    print()
