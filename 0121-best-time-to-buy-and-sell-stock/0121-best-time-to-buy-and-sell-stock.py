class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]   # smallest price seen so far
        max_profit = 0          # best profit so far

        for price in prices:
            # update minimum price
            if price < min_price:
                min_price = price

            # calculate profit if we sell today
            profit = price - min_price

            # update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit