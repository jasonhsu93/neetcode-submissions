class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        smallest = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            
            if prices[i] - smallest >= maxProfit:
                maxProfit = prices[i] - smallest

        return maxProfit


