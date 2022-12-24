import random

# W.L.O.G 車都在第 1 扇門
# 主持人開一扇門後，剩 n-2 扇門
N = 100000
for n in range(3, 11):
    win1 = 0
    for i in range(N):
        choose = random.randint(1, n)
        if choose == 1:
            win1 += 1

    win2 = 0
    for i in range(N):
        choose = random.randint(1, n)
        # 一開始沒選到門才有機會贏
        if choose != 1:
            choose = random.randint(1, n - 2)
            if choose == 1:
                win2 += 1
    print(
        "{} : {:.3f}[{:.3f}] up from {:.3f}".format(
            n, win2 / N, (n - 1) / (n * (n - 2)), win1 / N
        )
    )
