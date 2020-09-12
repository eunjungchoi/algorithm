# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
#
#
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
# Note:
#
# 0 ≤ N ≤ 30.

# 피보나치 수를 구하라.
# 각 수는 0과 1에서부터 시작된 앞 두 숫자의 합이 된다.

import collections


class Solution:
    memo = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        # 1. 기본 재귀 => 시간이 매우 오래 걸림.
        #         if N < 2:
        #             return N

        #         return self.fib(N-1) + self.fib(N-2)

        # 2. 상향식 = 타뷸레이션. iterative
        #         memo = collections.defaultdict(int)
        #         memo[0] = 0
        #         memo[1] = 1

        #         for i in range(2, N+1):
        #             memo[i] = memo[i-2] + memo[i-1]

        #         return memo[N]

        # 3. 하향식 = 메모이제이션. recursive. 클래스의 멤버변수에 저장공간.
        # 원래 브루트포스 풀이와 유사하게 재귀인데, 이미 계산한 값은 저장해뒀다가 바로 리턴.
        # 최종으로 찾는 값부터 시작해서 쭉 밑으로 파고들어가는 것.

        #         if N < 2:
        #             return N

        #         if self.memo[N]:
        #             return self.memo[N]

        #         self.memo[N] = self.fib(N-1) + self.fib(N-2)
        #         return self.memo[N]

        # 4. 두 변수만 사용해서 공간 절약하기. 공간복잡도 = O(1)
        x, y = 0, 1
        for i in range(N):
            x, y = y, x + y

        # N=1, i=0: x = 1, y 1,
        # N=2, i=1: x = 1, y 2
        # N=3, i=2: x = 2, y 3
        return x

        # 5. 행렬식으로 표현하기.  시간복잡고 O(log n)
        # 선형대수 관점에서 행렬의 n승을 계산하는 방식으로, 행렬 계산을 편리하게 하기 위해 numpy 모듈을 사용했으므로, leetcode에서 동작하지 않음.

        # M = np.matrix([[0, 1], [1, 1]])
        # vec = np.array([[0, 1]])
        #
        # return np.matmul(M ** n, vec)[0]


# 31 / 31 test cases passed.
# Status: Accepted
# Runtime: 16 ms
# Memory Usage: 13.7 MB
#
# Your runtime beats 99.90 % of python3 submissions.
# Your memory usage beats 86.94 % of python3 submissions.
