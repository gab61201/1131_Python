def point(card: str) -> float:
    cards = ["A"] + [str(n) for n in range(2, 11)]
    if card in cards:
        return cards.index(card) + 1
    elif card in ["J", "Q", "K"]:
        return 0.5


def ask_card(player_pt):
    while player_pt < 10.5:
        get_card = input()
        if get_card == "N":
            break
        player_pt += point(get_card.split()[-1])
    return player_pt


def main():
    players = int(input())
    player_bet = [0] + [int(bet) for bet in input().split()]
    player_point = [point(card) for card in input().split()]
    com_point = player_point[0]

    for i in range(1, players + 1):
        player_point[i] = ask_card(player_point[i])

    isAll_0 = len([p for p in player_point[1:] if p > 10.5]) == players
    isAll_max = player_point.count(10.5) == players
    while (
        not isAll_0
        and not isAll_max
        and com_point <= min(player_point[1:])
        and com_point != 10.5
    ):
        com_point += point(input())
        if com_point > 10.5:
            com_point = 0
            break

    com_earn = 0
    for i in range(1, players + 1):
        if player_point[i] == 10.5:
            com_earn -= player_bet[i]
            print(f"Player{i} {player_bet[i]:+d}")
        elif com_point >= player_point[i] or player_point[i] > 10.5:
            com_earn += player_bet[i]
            print(f"Player{i} {-player_bet[i]:+d}")
        elif com_point < player_point[i]:
            com_earn -= player_bet[i]
            print(f"Player{i} {player_bet[i]:+d}")
    print(f"Computer {com_earn:+d}")


if __name__ == "__main__":
    main()
