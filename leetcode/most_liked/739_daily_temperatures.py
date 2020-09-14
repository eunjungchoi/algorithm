# Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].

# 매일의 화씨 온도(F) 리스트 T를 받아, 더 따듯한 날씨를 위해서는 며칠을 더 기다려야 하는 지를 출력하라


from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 스택값 비교
        stack = [0]
        results = [0] * len(T)

        # 현재의 인덱스를 계속 스택에 쌓아두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의 온도 차이를 비교해서,
        # 더 높다면 스택의 값을 pop으로 꺼내고, 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를 정답으로 처리한다.
        for i, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                last = stack.pop()
                results[last] = i - last

            stack.append(i)

        return results


# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 492 ms
# Memory Usage: 17.2 MB
#
# Your runtime beats 71.54 % of python3 submissions.
# Your memory usage beats 89.19 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
