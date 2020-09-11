# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
#
# In one operation, you can choose any character of the string and change it to any other uppercase English character.
#
# Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# 대문자로 구성된 문자열 s가 주어졌을 때 k번 만큼의 변경으로 만들 수 있는, 연속으로 반복된 문자열의 가장 긴 길이를 출력하라.
# 투 포인터, 슬라이딩 윈도우, counter 이용
# 오른쪽 포인터에서 왼쪽 포인터 위치를 뺀 다음, 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같을 수 있는 수 중 가장 큰 최대 값
# 최대 길이를 찾는 문제이므로, right는 클수록 좋고, left는 작을수록 좋다.


import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()

        # 왼쪽 포인터와 오른쪽 포인터를 0으로 지정한 다음에 오른쪽 포인터 right는 계속 우측으로 한 칸씩 이동.
        # 이때 counter()를 이용해 가장 흔하게 등장하는 문자의 값을 계산해나감.

        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1

            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # 오른쪽 포인터는 계속 커지기 때문에 최댓값을 추출하기 위해서는 왼쪽 포인터는 0에서 움직이지 않는 게 가장 좋다.
            # 그러나 k 연산 횟수를 넘어선다면 어쩔 수 없이 left += 1 과 같이 왼쪽 포인터를 1 크게 한다.
            # k 초과시 왼쪽 포인터 이동.
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

            # 최대 길이 찾기
            # max_len = max(right - left, max_len)
            # 생략 가능.  한번 최댓값이 된 상태에서는 오른쪽 포인터가 한 칸 이동하면 왼쪽 포인터도 따라서 이동하면서 max_len 값은 바뀌지 않음.

        return right - left


# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 296 ms
# Memory Usage: 13.7 MB
#
# Your runtime beats 20.73 % of python3 submissions.
# Your memory usage beats 92.20 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
