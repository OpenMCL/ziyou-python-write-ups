number_map = {
    "1": ["一", "一"],
    "2": ["二", "兩"],
    "3": ["三", "三"],
    "4": ["四", "四"],
    "5": ["五", "五"],
    "6": ["六", "六"],
    "7": ["七", "七"],
    "8": ["八", "八"],
    "9": ["九", "九"],
    "0": ["零", "零"],
}

pre = ["", "十", "百", "千"]
base = ["", "萬", "億", "兆"]


def num_to_chinese(n):
    output = ""
    pre_order = 0
    base_order = 0
    print_base = False
    zero_appear = False
    for s in n[::-1]:
        if s == "0":
            if output:
                zero_appear = True
        else:
            if zero_appear:
                output = number_map["0"][0] + output
                zero_appear = False

            if print_base:
                output = base[base_order] + output
                print_base = False

            output = number_map[s][int(pre_order / 2)] + pre[pre_order] + output

        pre_order += 1
        if pre_order == 4:
            print_base = True
            pre_order = 0
            base_order += 1

    print(output)


if __name__ == "__main__":
    print("q(uit)")
    while True:
        s = input("> ")
        if s == "q":
            exit()

        n = str(int(s))
        if len(n) > 16:
            print("請輸入千兆數字")
            continue

        num_to_chinese(n)
