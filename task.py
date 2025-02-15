import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for j in range(coin, amount + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
                coin_used[j] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


# Тестування та порівняння ефективності
amount = 113

start_time = time.time()
greedy_result = find_coins_greedy(amount)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(amount)
dp_time = time.time() - start_time

print("Greedy result:", greedy_result, "Time:", greedy_time)
print("DP result:", dp_result, "Time:", dp_time)