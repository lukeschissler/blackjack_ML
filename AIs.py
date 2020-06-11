from random import random
from utils import hh_dict, sh_dict, sp_dict, dealer_dict



def hand_typer(hand, hand_sums, split):
    if 21 in hand_sums:
        return 'stand'
    elif len(hand) == 2 and hand[0].return_val() == hand[1].return_val() and not split:
        return 'split'
    elif (1, 11) in [x.return_val() for x in hand] and any(j < 10 for j in hand_sums):
        return 'soft'
    else:
        return 'hard'

def random_ai():
    return round(random())


def dealer_ai(**kwargs):
    hand_sum = kwargs.get("hand_sum")
    if any(j >= 17 and j < 22 for j in hand_sum):
        return "s"
    else:
        return "h"


def hits_ai(**kwargs):
    return "h"


def dd_ai(**kwargs):
    hand = kwargs.get('hand')
    if len(hand) == 2:
        if random() > 0.5:
            return 'd'
    return 'h'


def ml_ai(**kwargs):
    hand_sum = kwargs.get('hand_sum')
    dealer_card = kwargs.get('dealer_card')
    player = kwargs.get('player')

    hand_type = hand_typer(player.hands[-1], hand_sum, player.split)
    print(f'Hand: {player.hands[-1]},  hand_type: {hand_type}, D_card: {dealer_card.val}, Ante: {player.antes}')

    if hand_type == 'hard':
        return player.hard_table[hh_dict[min(hand_sum)]][dealer_dict[dealer_card.val]].lower()
    elif hand_type == 'soft':
        return player.soft_table[sh_dict[min(hand_sum)]][dealer_dict[dealer_card.val]].lower()
    elif hand_type == 'split':
        return player.split_table[sp_dict[min(hand_sum)]][dealer_dict[dealer_card.val]].lower()
    else:
        return 's'


def main():
    print(hh_dict)


if __name__ == "__main__":
    main()
