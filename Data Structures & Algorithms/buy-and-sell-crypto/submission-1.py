class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prefix = prices.copy()
        
        ma = 0
        for i in range(1, n):
            prefix[i] = min(prefix[i-1], prices[i]) 
        for i in range(-1, -n-1, -1):
            ma = max(ma, prices[i] - prefix[i]) 
        print(prefix)
        return ma