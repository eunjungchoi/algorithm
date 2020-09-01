# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [value for value, _ in collections.Counter(nums).most_common(k)]

        # pythonic way: zip()의 결과는 제너레이터를 반환. 실제값을 추출하기 위해 list()로 한번더 묶어 줌
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

        # using heap
        # freqs = collections.Counter(nums)
        # heap = []
        # for f in freqs:
        #     heapq.heappush(heap, (-freqs[f], f))
        #
        # result = []
        # for _ in range(k):
        #     result.append(heapq.heappop(heap)[1])
        #
        # return result


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 156 ms
# Memory Usage: 18.5 MB
#
# Your runtime beats 30.63 % of python3 submissions.
# Your memory usage beats 75.91 % of python3 submissions.


# using zip()
# Your runtime beats 95.64 % of python3 submissions.
# Your memory usage beats 71.80 % of python3 submissions.

# using heap
# Your runtime beats 98.63 % of python3 submissions.
# Your memory usage beats 26.08 % of python3 submissions.
