class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l = 0
        #r = len(prices) + 1
    
        n = len(prices)

        if n <= 1:
            return 0
        
        profit = []

        for i in range(n):
            for j in range(i+1, n):
                profit.append(prices[j] - prices[i])

        return max(max(profit), 0)