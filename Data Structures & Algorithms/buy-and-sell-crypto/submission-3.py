class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        i = 0
        j = 1
        min_price = prices[0] 

        while j < len(prices):
            profit = prices[j] - prices[i]
            result = profit if profit > result else result
            
            if prices[j] < min_price:
                min_price = prices[j]
                i = j
                j += 1
            else:
                j += 1

        return result 
            

        
