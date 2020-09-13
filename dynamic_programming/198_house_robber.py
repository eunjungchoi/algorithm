# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
#
#
# Constraints:
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400

# 당신은 전문털이범이다. 어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에 바로 옆집은 훔칠 수 없고 한 칸 이상 떠렁진 집만 가능하다. 각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어 있다. 훔칠 수 있는 가장 큰 금액을 출력하라.
# 다이내믹 프로그래밍을 떠올릴 수 있을 것 같다. 바로 옆집은 훔칠 수 없으니 현재 집과 옆집 숫자 중의 최댓값을 구하고, 한 집 건넛집까지의 최댓값과 현재 집의 숫자값과의 합을 구해서 두 수 중 더 높은 값이 정답이 된다.
import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # 1. 브루트 포스로 풀기  ==> timeout error
        #         def _rob(i: int) -> int:
        #             if i < 0:
        #                 return 0
        #             return max(_rob(i-1), _rob(i-2) + nums[i])
        #         return _rob(len(nums) - 1)

        # 2. 타뷸레이션 (상향식)
        # 이미 계산한 값은 memo에 저장하고 두 번이상 계산하지 않는다.
        # 재귀로 구현하는 메모이제이션보다 순회 방식인 타뷸레이션이 더 직관적이다.

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        memo = collections.OrderedDict()
        # 파이썬 딕셔너리는 3.7+부터 입력 순서가 유지된다.
        # 낮은 버전에서도 순서가 유지될 수 있도록 명시적으로 collections.OrderedDict()로 선언.

        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])

        return memo.popitem()[1]
        # 딕셔너리에서 가장 마지막 아이템을 추출할 때는 popitem()을 사용한다.
        # 그냥 pop()을 쓰려면 키를 지정해야 한다.


# 69 / 69 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 95.30 % of python3 submissions.
# Your memory usage beats 74.63 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
