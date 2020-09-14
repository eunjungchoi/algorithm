# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. brute force. 시간복잡도 O(n^2) ==> timeout error
        #         max_price = 0
        #         for i, price in enumerate(prices):
        #             for j in range(i, len(prices)):
        #                 max_price = max(max_price, prices[j] - price)

        #         return max_price

        # 2. 저점과 현재 값이 차이 계산. kadane's algorithm (카데인 알고리즘)
        # 시간 복잡도 O(n)
        profit = 0
        low = sys.maxsize

        # 최댓값과 최솟값을 계속 갱신
        for price in prices:
            low = min(price, low)  # 저점 갱신
            profit = max(profit, price - low)  # 최대 gap 이익  갱신

        return profit


# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Memory Usage: 14.9 MB
#
# Your runtime beats 44.61 % of python3 submissions.
# Your memory usage beats 98.25 % of python3 submissions.
