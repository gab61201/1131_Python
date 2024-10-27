def cards()->list:
    card_set = set(input().split())
    cards = ['A', 'J', 'Q', 'K'] + [str(i) for i in range(2,11)]
    all_cards = set()
    for color in ['S', 'H', 'D', 'C']:
        all_cards.update(c+color for c in cards)
    for card in card_set:
        if card not in all_cards:
            return 'Error input'
        elif len(card_set) != 5:
            return 'Duplicate deal'
        else:
            card = card[]
    return card_set

'''def card_type(card_set:set)->int:
    if 
'''
print(cards())