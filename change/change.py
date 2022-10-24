def find_no_check(coins, target):
    outs = []
    out = []
    for i in range(len(coins)):
        coin = coins[i]
        count = target // coin
        while count > 0:
            smaller_coins = []
            remaining_tmp = target - (count * coin)
            if remaining_tmp > 0:
                smaller_coins = find_no_check(coins[i + 1:], remaining_tmp)
                if smaller_coins is None:
                    count -= 1
                    continue
            outs.append(smaller_coins + [coin for _ in range(count)] + out)
            break
    if len(outs) == 0:
        return None
    min_combination = min(len(i) for i in outs)
    return next(i for i in outs if len(i) == min_combination)


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    coins.reverse()
    out = find_no_check(coins, target)
    if out:
        return out
    raise ValueError("can't make target with given coins")
