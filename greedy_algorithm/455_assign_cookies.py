# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size sj.

# If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
#
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.
#
# Example 1:
# Input: [1,2,3], [1,1]
#
# Output: 1
#
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1,
# you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:
# Input: [1,2], [1,2,3]
#
# Output: 2
#
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.

# 아이들에게 1개씩 쿠키를 나눠줘야 한다. 각 아이 child_i 마다 그리드 팩터 greed factor Gi 를 갖고 있으며, 이는 아이가 만족하는 최소 쿠키의 크기를 말한다.
# 각 쿠키 cookie_j는 크기 Sj를 갖고 있으며 Sj >= Gi 이어야 아이가 만족하며 쿠키를 받는다.
# 최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라.


from bisect import bisect
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        # 1. greedy algorithm
        child_i = cookie_j = 0
        
        # 만족하지 못할 때까지 그리디 진행
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

        # 2. binery search
        # 두 개의 리스트를 모두 번갈아가며 탐색하는 게 아니라, 하나의 리스트를 순회하면서 다른 하나는 이진 검색으로 찾음.
        # 찾아낸 인덱스가 현재 부여한 아이들보다 클 경우에는 더 줄 수 있다는 말이기 때문에 줄 수 있는 아이들의 수를 1명 더 늘린다.
        # result = 0
        #
        # for cookie_size in s:  # 쿠키를 순회하며
        #     # 이진 검색으로 더 큰 인덱스 탐색
        #     # bisect_left는 찾아낸 값의 해당 위치 인덱스를 리턴
        #     # bisect_right는 찾아낸 값의 다음 인덱스를 리턴
        #
        #     index = bisect.bisect_right(g, cookie_size)
        #     if index > result:
        #         result += 1
        #
        # return result


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 172 ms
# Memory Usage: 15.3 MB
#
# Your runtime beats 76.63 % of python3 submissions.
# Your memory usage beats 84.74 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.

