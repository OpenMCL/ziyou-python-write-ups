import random

hh, vv = chr(9473), chr(9475)
ml, mr = chr(9507), chr(9515)
nw, ne, sw, se = chr(9487), chr(9491), chr(9495), chr(9499)

n = int(input("> "))
r = random.randint(4, 9)
ran = [random.randint(0, 1) for x in range(r)]
door = [
    (
        (nw, hh, hh, ne),
        (ml, hh, hh, mr),
        (ml, hh, hh, se),
        (vv, " ", " ", " "),
        (vv, " ", " ", " "),
    ),
    (
        (nw, hh, hh, ne),
        (ml, hh, hh, mr),
        (sw, hh, hh, mr),
        (" ", " ", " ", vv),
        (" ", " ", " ", vv),
    ),
]
for i in range(5):
    for j in ran:
        for k in range(4):
            print(door[j][i][k], end="")
        print(" ", end=" ")
    print()
