poem = """
山山遠隔半山塘，心樂歸山世已忘。
樓閣擁山疑閬苑，村莊作畫實滄浪。
漁歌侑醉新絲竹，禪榻留題舊廟堂。
山近蘇城三四里，山峰千百映山光。
"""
poem = "".join([x for x in poem if x not in ["\n", "，", "。"]])

# part 1 山山遠隔
RC = 0  # right count
LC = len(poem)  # left count
for _ in range(2):
    t = "　" * 3
    t += poem[RC : RC + 2]
    RC += 2
    print(t)

# part 2 分成三部分，每部分 2行、2行、4行
for idx, rows in enumerate([2, 2, 4]):
    space_cc = 2 - idx
    word_cc = 4 - space_cc

    # 每一行細分出左半邊與右半邊來處理
    for i in range(rows):
        t = "　" * space_cc

        # left part
        _t = poem[LC - word_cc : LC]
        t += _t if i == 0 else _t[::-1]  # 設定迴轉
        LC -= word_cc

        # right part
        _t = poem[RC : RC + word_cc]
        t += _t if i == 0 else _t[::-1]  # 設定迴轉
        RC += word_cc

        print(t)
