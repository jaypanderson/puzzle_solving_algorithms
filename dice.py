def find_counter(index, dices):
    dice1 = dices[index]
    for i, dice2 in enumerate(dices):
        dice1_wins, dice2_wins = count_wins(dice1, dice2)
        if dice2_wins > dice1_wins:
            return i
    return -1




def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for one in dice1:
        for two in dice2:
            if one > two:
                dice1_wins += 1
            elif two > one:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    wins = {index: 0 for index in range(len(dices))}
    maxi = len(dices) - 1
    for i, dice1 in enumerate(dices):
        for j, dice2 in enumerate(dices[i + 1:], start=i + 1):
            dice1_wins, dice2_wins = count_wins(dice1, dice2)
            if dice1_wins > dice2_wins:
                wins[i] += 1
            elif dice2_wins > dice1_wins:
                wins[j] += 1

    for key, val in wins.items():
        if val == maxi:
            return key

    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    # strategy["first_dice"] = 0
    # for i in range(len(dices)):
    #     strategy[i] = (i + 1) % len(dices)

    best = find_the_best_dice(dices)
    if best == -1:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            strategy[i] = find_counter(i, dices)
    else:
        strategy["first_dice"] = best
    return strategy

if __name__ == "__main__":
    print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
