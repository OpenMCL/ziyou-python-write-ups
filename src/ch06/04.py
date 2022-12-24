p = "山中山路轉山崖，山客山僧山裡來。山客看山山景好，山杏山桃滿山開。"
p1 = "".join([x for x in p if x not in "，。"])
a = 28
for i in range(1, 8):
    b = a - i
    print("  " * (7 - i), end="")
    if i % 2:
        print("  ".join(p1[b:a]))
    else:
        print("  ".join(p1[b:a][::-1]))
    a = b
