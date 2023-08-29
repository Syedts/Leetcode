class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 99999999
        max_profit = 0 
        for n in prices:
            if n < min_val:
                min_val = n
            elif ((n-min_val) > max_profit):
                max_profit = n - min_val
        return max_profit