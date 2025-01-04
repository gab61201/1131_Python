from itertools import combinations


def cards():
    card_a = input().split()
    card_b = input().split()
    card_public = input().split()
    input_cards = set(card_a + card_b + card_public)

    card_num = {str(n): n for n in range(2, 11)}
    card_num.update({"A": 1, "J": 11, "Q": 12, "K": 13})

    for card in input_cards:
        if not card[1:] in card_num.keys() or not card[0] in ["S", "H", "D", "C"]:
            print("Error input")
            exit()
    if len(input_cards) != 8:
        print("Duplicate deal")
        exit()
    return card_a, card_b, card_public


def cardType(cards: list):
    card_num = {str(n): n for n in range(2, 11)}
    card_num.update({"A": 1, "J": 11, "Q": 12, "K": 13})
    card_seqs = [card_num[card[1:]] for card in cards]
    card_types = [card[0] for card in cards]
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
    card_a, card_b, card_public = cards()
    comb_a = combinations(card_a + card_public, 5)
    max_a = max(cardType(card) for card in comb_a)
    comb_b = combinations(card_b + card_public, 5)
    max_b = max(cardType(card) for card in comb_b)
    if max_a > max_b:
        print("A", max_a)
    elif max_b > max_a:
        print("B", max_b)
    else:
        print("Tie")


if __name__ == "__main__":
    main()
