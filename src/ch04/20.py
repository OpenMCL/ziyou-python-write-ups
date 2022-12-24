import random

# W.L.O.G 車都在第 1 扇門
# 交換:
# 一開始選 1，交換成 3
# 一開始選 2，交換成 3
# 一開始選 3，交換成羊
win = 0
for i in range(10000):
    choose = random.randint(1, 3)
    if choose == 1:
        win += 1

print("no change:", win / 10000)

win = 0
for i in range(10000):
    choose = random.randint(1, 3)
    if choose != 1:
        win += 1

print("change:", win / 10000)
