class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxPro = max(maxPro, prices[i] - minPrice)
            else:
                minPrice = min(prices[i], minPrice)
        return maxPro