import random

count = [0 for i in range(6)]
count1 = [[0] * 5 for x in range(6)]
for i in range(1600000):
    ran = random.randint(0, 4) * 2 + 1
    cr = int((ran - 1) / 2)
    step = random.randint(0, 1) * 2 - 1
    ran += step
    for j in range(2):
        step = random.randint(0, 1) * 2 - 1
        ran += step
        if ran < 0 or ran > 10:
            break
        step = random.randint(0, 1) * 2 - 1
        ran += step
    if ran <= 0:
        count[0] += 1
        count1[0][cr] += 1
    elif ran >= 10:
        count[-1] += 1
        count1[-1][cr] += 1
    else:
        count[int(ran / 2)] += 1
        count1[int(ran / 2)][cr] += 1
for k in range(6):
    print(str(int(count[k] / 10000 + 0.5)) + "/160" + "=>", end="")
    for m in range(4):
        print(str(int(count1[k][m] / 10000 + 0.5)) + "+", end=" ")
    print(int(count1[k][4] / 10000 + 0.5))
