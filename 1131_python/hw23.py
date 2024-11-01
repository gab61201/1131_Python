def point(card: str) -> float:
    cards = ["A"] + [str(n) for n in range(2, 11)]
    if card in cards:
        return cards.index(card) + 1
    if card in ["J", "Q", "K"]:
        return 0.5


def main():
    player_point = point(input())
    com_point = point(input())
    player_conti = True
    com_conti = True

    while player_point > 0 and com_point > 0:
        if not (player_conti or com_conti):
            break

        if player_conti:
            if input() == "Y":
                player_point += point(input())
            else:
                player_conti = False
        if player_point > 10.5:
            player_point = 0
            break

        if (com_point < player_point or com_point <= 8) and com_conti:
            com_point += point(input())
        else:
            com_conti = False
        if com_point > 10.5:
            com_point = 0
            break

    if com_point == player_point:
        print("it's a tie")
    elif com_point > player_point:
        print("computer win")
    elif com_point < player_point:
        print("player win")


main()
