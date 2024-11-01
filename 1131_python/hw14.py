def play() -> list:
    score = [int(input())]
    if score[0] != 10:
        score.append(int(input()))
    return score


def total_score(games: list) -> int:
    score = int()
    for round in range(10):
        if round == 9:
            score += sum(games[round])
            break
        if (games[round][0] == 10) and (games[round + 1][0] == 10):
            score += 20 + games[round + 2][0]
        elif games[round][0] == 10:
            score += 10 + sum(games[round + 1])
        elif sum(games[round]) == 10:
            score += 10 + games[round + 1][0]
        else:
            score += sum(games[round])
    return score


def main():
    play_game = [play() for _ in range(10)]
    extra_points = int()
    if play_game[-1][0] == 10:
        extra_points = int(input()) + int(input())
    elif sum(play_game[-1]) == 10:
        extra_points = int(input())
    print(total_score(play_game) + extra_points)


if __name__ == "__main__":
    main()
