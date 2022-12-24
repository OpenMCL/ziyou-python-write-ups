import random

count = 0
for j in range(1000000):
    ran = [random.randint(1, i) for i in range(3, 7)]
    ran.sort()
    if ran[0] + 1 == ran[1] and ran[1] + 1 == ran[2] and ran[2] + 1 == ran[3]:
        count += 1
print(count / 1000000)
