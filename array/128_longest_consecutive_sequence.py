# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        # time complexity O(1)의 핵심.
        # python에서 set은  hashtable로 구현되어 있어서  lookup/insert/delete 모두 O(1)
        max_length = 0

        for num in nums:
            if num - 1 not in nums:   # 1만큼 작은 값이 없으면,  = 값이 속한 연속 시퀀스에서 가장  작은 값일 경우
                bigger = num + 1
                while bigger in nums:    # 1만큼 큰 수가 리스트에 있으면  다시 1만큼 큰 수를 찾아냄.  계속 루프.
                    bigger = bigger + 1

                max_length = max(max_length, bigger - num)   # 가장 큰 연속 수를 찾아내서 그 수와 현재 수와의 차이를 계산해서 max length 업데이트

        return max_length


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 15.2 MB
#
# Your runtime beats 99.51 % of python3 submissions.
# Your memory usage beats 28.32 % of python3 submissions.
