import random

count = [0 for i in range(6)]
for _ in range(1600000):
    ran = random.randint(0, 4) * 2 + 1
    step = random.randint(0, 1) * 2 - 1
    ran += step
    for j in range(2):
        if j == 1 and (ran == 2 or ran == 8):
            ran = 100
        step = random.randint(0, 1) * 2 - 1
        ran += step
        if ran < 0 or ran > 10:
            break
        if j == 0 and ran == 5:
            ran = 100
        step = random.randint(0, 1) * 2 - 1
        ran += step
    if ran <= 0:
        count[0] += 1
    elif ran > 13:
        ran = 100
    elif ran >= 10:
        count[-1] += 1
    else:
        count[int(ran / 2)] += 1
for k in count:
    print("{:>3}".format(int(k / 10000 + 0.5)), end="  ")
print()
for _ in range(6):
    print("---", end="  ")
print()
for _ in range(6):
    print("160", end="  ")
