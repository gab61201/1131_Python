def main():
    game_9 = [int(input())]
    if game_9[0] != 10:
        game_9 += [int(input())]

    game_10 = [int(input()), int(input())]
    if game_10[0] == 10 or sum(game_10) == 10:
        game_10 += [int(input())]

    score_list = game_9 + game_10
    if game_9[0] == 10:
        score_list += score_list[1:3]
    elif sum(game_9) == 10:
        score_list.append(score_list[2])
    print(sum(score_list))

if __name__ == '__main__':
    main()