# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].


class Solution:
    """

    X는 각 숫자를 개별적으로 180도 돌린 후에 X와 다른 유효한 숫자를 얻게 되면 좋은 숫자다.
    각각의 자릿수는 회전해야 한다 - 우리는 그것을 그냥 두기로 선택할 수 없다.
    각 자리가 회전 후에 digit으로 남아 있으면 숫자가 유효하다.
    0, 1, 8은 자전한다.
    2와 5는 서로 회전한다 (이 경우 다른 방향으로 회전한다, 다시 말하면 2 또는 5는 거울에 비친다).
    6과 9는 서로 회전한다.
    나머지 숫자는 다른 숫자로 회전하지 않고 무효가 된다.
    이제 양수 N이 주어질 때, 1에서 N까지 X는 몇 개인가?
    """

    def rotatedDigits(self, N: int) -> int:
        # 1. brute force
        # 3, 4, 7 중에 하나라도 있으면 not good. 하나도 없어야.
        # 2, 5, 6, 9 중에 하나라도 없으면  회전후 x가 같기 때문에 not good.  하나라도 있어야.
        # time complexity: O(N log N). for each x, we check each digit
        # space complexity: O(logN), the space stored either by the string,
        # or the recursive call stack of the function good.
        result = 0
        for i in range(1, N + 1):
            s = str(i)
            result += (
                    all(num not in "347" for num in s)
                    and any(num in "2569" for num in s)
            )

        return result

# 50 / 50 test cases passed.
# Status: Accepted

# brute force
# Runtime: 116 ms
# Memory Usage: 14.1 MB
# Your runtime beats 40.89 % of python3 submissions.
# Your memory usage beats 16.72 % of python3 submissions.

    def rotatedDigits1(self, N):
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = list(map(int, str(N)))
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7 ** (len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3 ** (len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))

    def rotatedDigits2(self, N: int) -> int:
        # dynamic programming on digits
        # 2, 5, 6, 9 중에 하나는 써야 한다.
        # i: 얼마나 많은 숫자를 썼는지
        # equality_flag: N의 j번째 숫자보다 작은 j 번째 숫자를 썼는지
        # involution_flag: 2569 중 하나를 썼는지

        # dp(i, equality_flag, invoution_flag) 는 위의 조건에 해당하는 N의 접미사를 쓰는 방법의 수. 우리가 원하는 답은 dp(0, True, False) 이다.

        # 알고리즘:
        # equality_flag가 참일 경우, i번째 digit은 최대 N의 i번째 수가 된다. 각 숫자 d에 대해 현재 설정된 flag를 기준으로 d를 쓸 수 있는지 판단한다.

        A = list(map(int, str(N)))
        memo = {}

        def dp(i, equality_flag, involution_flag):
            if i == len(A):
                return +involution_flag

            if (i, equality_flag, involution_flag) not in memo:
                result = 0
                for d in range(A[i] + 1 if equality_flag else 10):
                    if d in {3, 4, 7}: continue
                    result += dp(i + 1, equality_flag and d == A[i], involution_flag or d in {2, 5, 6, 9})

                memo[i, equality_flag, involution_flag] = result

            return memo[i, equality_flag, involution_flag]

        return dp(0, True, False)


# 50 / 50 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 14.3 MB
#
# Your runtime beats 99.70 % of python3 submissions.
