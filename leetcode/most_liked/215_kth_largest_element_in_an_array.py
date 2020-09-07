# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1) using heapq
        #         heap = []
        #         for n in nums:
        #             heapq.heappush(heap, -n)
        #         for _ in range(k-1):
        #             heapq.heappop(heap)
        #         return -heapq.heappop(heap)

        # 2) using heapify
        #         heapq.heapify(nums)
        #         for _ in range(len(nums)-k):
        #             heapq.heappop(nums)
        #         return heapq.heappop(nums)

        # 3) using heapq. nlargest
        # return heapq.nlargest(k, nums)[-1]

        # 4) using 정렬
        nums.sort()
        return nums[-k]


# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 14.8 MB
#
# Your runtime beats 88.64 % of python3 submissions.
# Your memory usage beats 82.62 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
