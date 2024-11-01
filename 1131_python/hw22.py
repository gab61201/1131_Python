def cards(input_cards):
    card_num = {str(n): n for n in range(2, 11)}
    card_num.update({"A": 1, "J": 11, "Q": 12, "K": 13})
    card_seqs, card_types = [], []
    for card in input_cards:
        num = card[:-1]
        if num in card_num.keys() and card[-1] in ["S", "H", "D", "C"]:
            card_seqs.append(card_num[num])
            card_types.append(card[-1])
        else:
            print("Error input")
            exit()
    return card_seqs, card_types


def cardType(card_seqs: list, card_types: list):
    count_card = [
        card_seqs.count(card) for card in card_seqs
    ]  # 生成一個計算牌面數字出現次數的list
    for num in card_seqs:  # ex: 1, 2, 3, 12, 13
        seq = {
            num + n if num + n <= 13 else num + n - 13 for n in range(5)
        }  # 若生成數字超過13，則減13
        if seq == set(card_seqs):
            straight = True
            break
        else:
            straight = False
    if straight and len(set(card_types)) == 1:
        return 9
    if 4 in count_card:
        return 8
    if (2 in count_card) and (3 in count_card):
        return 7
    if len(set(card_types)) == 1:
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
    players = list()
    all_cards = set()
    for _ in range(int(input())):
        input_cards = input().split()
        name = input_cards.pop(0)
        all_cards = all_cards.union(set(input_cards))
        card_info = cards(input_cards)
        players.append({"name": name, "score": cardType(*card_info)})
    players = sorted(players, key=lambda x: x["score"], reverse=True)
    if len(all_cards) == len(players)*5:
        for p in players:
            print(p["name"], p["score"])
    else:
        print("Duplicate deal")


if __name__ == "__main__":
    main()
