class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        best_buy = prices[0]

        for i in range(1, len(prices)):
            current_profit = prices[i] - best_buy
            if max_profit < current_profit:
                max_profit = current_profit

            if best_buy > prices[i]:
                best_buy = prices[i]
        return max_profit