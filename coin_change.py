def coin_change(coins, amount):
    dp = [10] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] < 10 else -1


def change(amount, coins):
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 1
    for i in range(1, len(coins) + 1):
        dp[i][0] = 1
        for j in range(1, amount + 1):
            dp[i][j] += dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0)
    return dp[len(coins)][amount]


def coin_change_2(coins, amount):
    tmp, res = [], []

    def helper(start, total):
        if start >= len(coins) or total < 0:
            return
        if total == 0:
            res.append('+'.join(map(str, tmp)))
            return
        tmp.append(coins[start])
        helper(start, total - coins[start])
        tmp.pop()
        helper(start + 1, total)
    helper(0, amount)
    return res


def coin_change_3(coins, amount):
    dp, select = [10] * (amount + 1), [-1] * (amount + 1)
    dp[0], select[0] = 0, 0
    for i in range(1, amount + 1):
        pick = 0
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                pick = coin
        select[i] = pick
    if dp[-1] == 10:
        return -1
    res = []
    remain = amount
    while remain > 0:
        res.append(select[remain])
        remain -= select[remain]
    return f'''{' + '.join(map(str, res))} = {amount}'''


if __name__ == '__main__':
    print('leetcode 322')
    print(coin_change([1, 2, 5], 11))
    print(coin_change([2], 3))
    print(change(5, [1, 2, 5]))
    print(change(10, [10]))
    print(coin_change_2([1, 2, 5], 11))
    print(coin_change_3([1, 2, 5], 11))

