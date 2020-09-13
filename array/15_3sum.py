# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        # 1. brute force.
        # 3 pointers 활: 시간복잡도 O(n^3) ==> timeout error
        # keys: i, j, k

        # for i in range(len(nums) - 2):
        #     # 중복된 값 건너뛰기
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1, len(nums) - 1):
        #         if j > i+1 and nums[j] == nums[j-1]:
        #             continue
        #         for k in range(j+1, len(nums)):
        #             if k > j+1 and nums[k] == nums[k-1]:
        #                 continue
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 results.append((nums[i], nums[j], nums[k]))
        # return results

        # 2. two pointers : 일반적으로 배열이 정렬되어 있을 때 더 유용함.  시간복잡도 O(n^2)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ < 0:  # sum이 0보다 작으면 값을 더 키워야 하므로 left를 한 칸 우측으로.
                    left += 1
                elif sum_ > 0:  # sum이 0보다 크면 값을 더 줄여야 하므로 right을 한 칸 왼쪽으로.
                    right -= 1
                else:
                    # sum = 0 일 때는 정답이므로 결과를 리스트 변수 results에 추가.
                    results.append((nums[i], nums[left], nums[right]))

                    # left, right 양 옆으로 동일한 값이 있을 수 있으므로 이를 left += 1, right -= 1 을 반복해서 스킵하도록 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results


# 318 / 318 test cases passed.
# Status: Accepted
# Runtime: 888 ms
# Memory Usage: 16.6 MB
#
# Your runtime beats 73.33 % of python3 submissions.
# Your memory usage beats 98.11 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
