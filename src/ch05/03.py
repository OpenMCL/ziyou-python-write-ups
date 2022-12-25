import random

poker = [x for x in range(1, 53)]
count = 0
for _ in range(1000000):
    random.shuffle(poker)
    poker1 = [poker[m] for m in range(0, 5)]
    poker1.sort(key=lambda x: x % 13)
    if (
        poker1[0] % 13 + 1 == poker1[1] % 13
        and poker1[1] % 13 + 1 == poker1[2] % 13
        and poker1[2] % 13 + 1 == poker1[3] % 13
        and poker1[3] % 13 + 1 == poker1[4] % 13
    ):
        if (
            poker1[0] + 1 == poker1[1]
            and poker1[1] + 1 == poker[2]
            and poker1[2] + 1 == poker1[3]
            and poker1[3] + 1 == poker[4]
        ):
            print(poker1)
            continue
        # print(poker1)
        count += 1
print(count / 1000000)
