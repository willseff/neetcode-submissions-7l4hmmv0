
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import sys
        sys.setrecursionlimit(10000)
        min_coins = min(coins)

        def mem(amount, cache):
            if amount in cache:
                return cache[amount]
            nonlocal min_coins
            nonlocal coins
            if amount == 0:
                cache[0] = 0
                return 0
            if amount in coins:
                cache[amount] = 1
                return 1
            if amount < min_coins:
                cache[amount] = -1
                return -1
            result_list = []
            for coin in coins:
                if amount > coin:
                    result_list.append(mem(amount - coin, cache))
            valid = [x for x in result_list if x != -1]
            if not valid:
                cache[amount] = -1
                return -1
            cache[amount] =  min(valid) + 1

            return cache[amount]
        
        return mem(amount, {})