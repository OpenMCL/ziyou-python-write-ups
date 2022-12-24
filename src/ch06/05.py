poem = "山裡有山路轉彎，高山流水響潺潺。" "深山百鳥聲聲叫，路上行人步步難。" "勸君莫作雲遊客，孤身日日在山間。" "人人說道華山好，我道華山第八山。"
poem1 = "".join([x for x in poem if x not in "。，"])
ns = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4]
p1, p2 = poem1[-28:][::-1], poem1[:28]
a = 0
for i in range(10):
    for j in range(3):
        if j == 0:
            b = a + ns[i]
        if i % 2 == 0:
            print(
                "  " * (4 - ns[i]) + p1[a:b][::-1] + p2[a:b] + "  " * (4 - ns[i]),
                end="  ",
            )
        else:
            print(
                "  " * (4 - ns[i]) + p1[a:b] + p2[a:b][::-1] + "  " * (4 - ns[i]),
                end="  ",
            )
    a = b
    print()
