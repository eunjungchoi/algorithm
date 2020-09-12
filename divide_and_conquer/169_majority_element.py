# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2

# 과반수를 차지하는 엘리먼트를 출력하라
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 1. brute force ==> timeout error 를 일으킴
        #         for n in nums:
        #             if nums.count(n) > len(nums) // 2:
        #                 return n

        # 2. dynamic programming
        # 한 번 계산한 값은 저장해서 재활용
        # 계산되지 않았던 값이 들어오면 항상 0이고 그때만 카운트를 계산.
        # 메모이제이션을 이용한 매우 간단한 다이나믹 프로그래밍 풀이.
        #         counts = collections.defaultdict(int)

        #         for num in nums:
        #             if counts[num] == 0:
        #                 counts[num] = nums.count(num)

        #             if counts[num] > len(nums) // 2:
        #                 return num

        # 3. pythonic way
        # 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트 일 것이다.
        # 매우 직관적이며 쉬운 알고리즘.
        # return sorted(nums)[len(nums) // 2]

        # 4. divide and conquer
        # 쪼갠 다음 과반수 후보군에 해당하는 엘리먼트만 리턴하면서 계속 위로 올려주면 (백트래킹) 최종적으로 정답만 남게 됨.

        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        # 최소 단위로 쪼개질 때 해당하는 값을 리턴하게 됨.

        # 백트래킹될 때 처리하는 부분. 정복 부분
        # a가 만약 현재 분할된 리스트 nums에서 과반수를 차지한다면 해당 인덱스는 1
        # 아니면 인덱스가 0이 되어 b를 리턴

        # ex. [1, 2, 1, 3, 1, 4, 1, 1] 같은 입력값에서도 비둘기집 원리에 따라 반드시 [1,1]이 함께 위치하는 분할이 존재한다.
        # 따라서 1은 최소 한 번 이상 반드시 리턴되고, 계속 상위 분할에서 과반수를 넘어서서 끝까지 살아남아 최종적으로 1을 정답으로 리턴하게 된다.
        return [b, a][nums.count(a) > half]


# 46 / 46 test cases passed.
# Status: Accepted
# Runtime: 160 ms
# Memory Usage: 14.9 MB
#
# Your runtime beats 99.05 % of python3 submissions.
# Your memory usage beats 99.12 % of python3 submissions.

# 다이내믹 프로그래밍과 pythonic way가 가장 빠름
