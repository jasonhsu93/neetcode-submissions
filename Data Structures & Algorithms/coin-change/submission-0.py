class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # idea is to have a loop that goes from 1 to amount, while the loop increases in value
        # say at 1 2 3 4, we would check if each coin in coins can reach the amount needed. And we would store
        # the answer along the way
        # ex. [1,5,10] amount = 12
    # at i = 1, we would check i - 1 >= 0 and see if dp[i - 1] exists, dp in this case would store the 
        # minimum number of coins needed for the amount i - 1 and so the amount of coins needed for 1 would be
        # dp[0] + 1 in this case, we repeat this until dp[amount] is reached

        # dp array to store number of coins needed for each integer value up to amount
        dp = [-1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != -1:
                    dp[i] = 1 + dp[i-coin] if dp[i] == -1 else min(dp[i], 1 + dp[i-coin])
        
        return dp[amount]