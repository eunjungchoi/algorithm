# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45

# 당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다.
# 매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라.

# 경우의 수를 하나씩 그려보면 기본적으로 <피보나치 수>와 동일한 유형의 문제다.

import collections


class Solution:
    memo = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # 1. 재귀로 풀기. 피보나치 수열과 완전히 동일한 풀이  ==> timeout error
        #         return self.climbStairs(n-1) + self.climbStairs(n-2)

        # 2. 메모이제이션
        if self.memo[n]:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memo[n]


# 45 / 45 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14 MB
#
# Your runtime beats 57.98 % of python3 submissions.
# Your memory usage beats 21.93 % of python3 submissions.
