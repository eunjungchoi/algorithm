# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

# 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.

# 괄호를 어디에 추가하느냐에 따라 다양한 조합이 가능하다.
# 모든 조합을 계산해야하는데 분할 정복으로 가능하다.

# *, -, + 연산자가 등장할 때 좌/우 분할을 하고 각각 계산 결과를 리턴한다.
# ex. 3-4*5 는 -17과 -5 라는 복수 개의 계산 결과를 갖게 되며 최종적으로 2 * [-17, -5] 의 계산 결과인 [-34, -10]을 리턴하게 된다.
# 우측으로는 각각 다른 계산 결과도 리턴 받게 된다.

from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))

            # eval() 함수는 문자열을 파싱하고 파이썬 표현식으로 처리해주는 역할
            return results

        # 분할 결과를 리턴받으려면 이처럼 input이 숫자형일 때 리턴하게 한다.
        # 분할의 결과가 최종적으로 숫자형인 타입을 재귀의 최종 결과로 리턴.

        if input.isdigit():
            return [int(input)]

        results = []

        for index, value in enumerate(input):
            if value in "-+*":  # 연산자를 기준으로 재귀로 left, right를 계속 분할하고
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                # 분할된 값은 compute() 함수로 계산한 결과를 extend로 확장
                results.extend(compute(left, right, value))

        return results


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 64 ms
# Memory Usage: 14 MB
#
# Your runtime beats 12.04 % of python3 submissions.
# Your memory usage beats 49.32 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
