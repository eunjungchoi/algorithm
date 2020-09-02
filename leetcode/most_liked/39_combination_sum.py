# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# Each element of candidate is unique.
# 1 <= target <= 500
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                results.append(path)
                return

                # 자신부터 하위 원소까지의 나열  재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
                # dfs(csum - candidates[i], 0, path + [candidates[i]])  <= i를 0으로 바꾸면 순열. 매번 처음 값부터 계산.

        dfs(target, 0, [])
        return results


# 168 / 168 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Memory Usage: 14 MB
#
# Your runtime beats 72.19 % of python3 submissions.
# Your memory usage beats 37.22 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고. 
