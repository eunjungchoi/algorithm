# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(index, path):
            # 매번 결과 추가
            results.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return results


# 10 / 10 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 96.05 % of python3 submissions.
# Your memory usage beats 28.90 % of python3 submissions.


