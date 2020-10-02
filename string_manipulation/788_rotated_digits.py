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
