# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums))

        result = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과에 추가
            if len(elements) == 0:
                result.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

#
# dfs([1, 2, 3])
#
# == 앞자리 1일 때
# e = 1
# next_element = [2, 3]
# prev_element = [1]
# dfs([2, 3])
# e = 2
# next_element = [3]
# prev_element = [1, 2]
# dfs([3])
# e = 3
# next_element = []
# prev_element = [1, 2, 3]
# dfs([])
# result.append(prev_elements)
#
# prev_element.pop()   // elements = [3]일 때.
# prev_element = [1, 2]
#
# prev_element.pop()   // elements = [2, 3] 일 때.
# prev_element = [1]
# e = 3
# next_element = [2]
# prev_element = [1, 3]
# dfs([2])
# e = 2
# next_element = []
# prev_element = [1, 3, 2]
# dfs([])
# result.append(prev_elements)
#
# prev_element.pop()  // elements = [2] 일 때.
# prev_element = [1, 3]
#
# prev_element.pop()  //
# prev_element = [1]    // elements = [1, 2, 3] 일 때로 돌아옴.
#
# ===== 여기서 부터 앞자리 2
# e = 2
# next_element = [1, 3]
# prev_element = [2]
# dfs([1,3])
# e = 1
# next_element = [3]
# prev_element = [2, 1]
# dfs([3])
# e = 3
# next_element = []
# prev_element = [2, 1, 3]
# dfs([])
# result.append(prev_element)
#
# prev_element.pop()  //  elements = [3] 일 때
# prev_element = [2, 1]
#
# prev_element.pop()  // elements = [1, 3]일 때
# prev_element = [2]
#
# e = 3
# next_element = [1]
# prev_element = [2, 3]
# dfs([1])
# e = 1
# next_element = []
# prev_element = [2, 3, 1]
# dfs([])
# result.append(prev_element)
#
# prev_element.pop()   //  elements = [1]일 때
# prev_element = [2, 3]
#
# prev_element.pop()  // elements = [1, 3] 일 때
# prev_element = [2]
#
# prev_element.pop()
# prev_element = []
#
# --- 여기서부터 앞자리 3
#
# e = 3
# next_element = [1, 2]
# prev_element = [3]


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 61.51 % of python3 submissions.
# Your memory usage beats 29.41 % of python3 submissions.

# using itertools
# Your runtime beats 92.69 % of python3 submissions.
# Your memory usage beats 85.54 % of python3 submissions.



