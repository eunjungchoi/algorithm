# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

# 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # 1. 브루트 포스로 계산  ==> timeout error
        # 파이썬에서는 슬라이싱과 내장 함수를 사용해 풀이 가능

        #         if not nums:
        #             return nums

        #         r = []
        #         # k = 슬라이딩 윈도우의 크기
        #         for i in range(len(nums) - k + 1):
        #             r.append(max(nums[i:i+k]))  # <= max() 계산하는 부분에서 최적화가 필요함.
        #         return r

        # 2. 큐를 이용한 최적화

        # 정렬되지 않은 슬라이딩 윈도우에서 최댓값 계산을 O(n) 이내로 줄일 수 있는 방법이 없다.
        # 따라서 가급적 최댓값 계산을 최소화하기 위해 이전의 최댓값을 저장해뒀다가 한칸씩 이동할 대 새 값에 대해서만 더 큰 값인지 확인하고
        # 최댓값이 윈도우에서 빠지게 되는 경우에만 다시 전체를 계산하는 형태로 개선한다면, 계산량을 획기적으로 줄일 수 있다.
        # 선입선출 FIFO 형태로 풀이할 수 있기 때문에, 큐를 사용한다.

        results = []
        current_max = float('-inf')  # 시스템이 지정할 수 있는 가장 낮은 값을 지정하여 초기화.
        window = collections.deque()  # 큐 사용이 필요할 경우, 기능이 많고 성능이 좋은 데크 사용.

        for i, v in enumerate(nums):
            window.append(v)

            # k 만큼 일단 값을 채워넣는다.
            if i < k - 1:
                continue

            # 아직 최댓값이 반영된 상태가 아니라면, 현재 윈도우 전체의 최댓값 계산.
            if current_max == float('-inf'):
                current_max = max(window)

            # 이미 최댓값이 존재한다면, 새로 추가된 값이 기존 최댓값보다 더 큰 경우에만 최댓값 교체.
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')

        return results


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 300 ms
# Memory Usage: 26.3 MB
#
# Your runtime beats 97.07 % of python3 submissions.
# Your memory usage beats 63.24 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
