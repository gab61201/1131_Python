def player_points()->dict:
    player = {'name':input(), 'points':int()}
    for _ in range(3):
        try:
            player['points'] += int(input())
        except ValueError:
            player['points'] += 0.5
    if player['points'] > 10.5:
        player['points'] = 0
    return player

def game_1(player:dict, banker:dict):
    if (player['points'] == 0) or (player['points'] < banker['points']):
        print(f'{banker["name"]} Win')
    elif player['points'] > banker['points']:
        print(f'{player["name"]} Win')
    elif player['points'] == banker['points']:
        print('Tie')

def game_2(player:dict, banker:dict):
    if player['points'] == banker['points']:
        print('Tie')
    elif player['points'] > banker['points']:
        print(f'{player["name"]} Win')
    elif player['points'] < banker['points']:
        print(f'{banker["name"]} Win')

if __name__ == '__main__':
    Player = player_points()
    Banker = player_points()
    game_1(Player,Banker)
    game_2(Player,Banker)