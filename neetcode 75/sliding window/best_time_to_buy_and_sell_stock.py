# problem:
# given an array prices where price[i] is the price of stock on ith day
# can choose a single day to buy and a diff day in future to sell
# return max profit achievable or else 0 if no good transactions
# 
# O(n) soln:
# sliding window tech
# l = 0
# highest = 0
# iterate r through arr list
# if l > r:
#   # want to buy low sell high so if l > r buy at r
#   l = r
# else:
#   # calculate and update profit
#   profit = prices[l] - prices[r]
#   highest = max(highest, profit)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        highest = 0
        l = 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                highest = max(highest, profit)
        return highest