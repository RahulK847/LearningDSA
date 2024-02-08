def coinChange(coins, amount):
    coins = set(coins)
    dp = [float('inf')]*amount+1
    for i in range(1, amount+1)
        if i in coins:
            dp[i] = 1
        else:
            




coins = [ 1, 2, 5]
amount = 11
print(coinChange(coins, amount))