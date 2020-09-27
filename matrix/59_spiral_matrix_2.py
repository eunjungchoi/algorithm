# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
from typing import List


class Solution:
    # Solution 1: Build it inside-out - 44 ms, 5 lines
    # Start with the empty matrix, add the numbers in reverse order until we added the number 1.
    # Always rotate the matrix clockwise and add a top row:

    #     ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
    #                      |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
    #                                          |8 7|      |7 6 5|
    def generateMatrix(self, n: int) -> List[List[int]]:
        res, lo = [[n * n]], n * n

        while lo > 1:
            lo, hi = lo - len(res), lo
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]

        return res


# 20 / 20 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 69.17 % of python3 submissions.
# Your memory usage beats 41.96 % of python3 submissions.
