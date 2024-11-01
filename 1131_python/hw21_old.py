def cards() -> list:
    card_num = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]
    card_face = ["S", "H", "D", "C"]
    input_cards = input().split()
    card_seq, card_type = [], []
    for card in input_cards:
        if card[:-1] in card_num and card[-1] in card_face:
            number = card_num.index(card[:-1]) + 1
            card_seq.append(number)
            card_type.append(card[-1])
        else:
            return print("Error input")
    if len(set(input_cards)) != 5:
        return print("Duplicate deal")
    return card_seq, card_type


def cardType(card_seq: list, card_type: list):
    count_card = [
        card_seq.count(card) for card in card_seq
    ]  # 生成一個計算牌面數字出現次數的list
    straight = False
    for num in card_seq:  # ex: 1, 2, 3, 12, 13
        seq = {num + n if num + n <= 13 else num + n - 13 for n in range(5)}  # 若生成數字超過13，則減13
        if seq == set(card_seq):
            straight = True
            break
    if straight and len(set(card_type)) == 1:
        return 9
    if 4 in count_card:
        return 8
    if (2 in count_card) and (3 in count_card):
        return 7
    if len(set(card_type)) == 1:
        return 6
    if straight:
        return 5
    if 3 in count_card:
        return 4
    if count_card.count(2) == 4:
        return 3
    if count_card.count(2) == 2:
        return 2
    return 1


def main():
    card_seq, card_type = cards()
    if card_seq and card_type:
        print(cardType(card_seq, card_type))


if __name__ == "__main__":
    main()
