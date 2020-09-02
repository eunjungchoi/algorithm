# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색했을 때, path를 result 에 추가하고 백트래킹.
            if len(path) == len(digits):
                result.append(path)
                return

                # 입력값 자릿수 개수만큼 반복
            for i in range(index, len(digits)):
                for char in dic[digits[i]]:  # 입력값 digits의 i 번째 글자의 value 문자열 순회하며 문자 하나씩을 가져와
                    dfs(i + 1, path + char)  # path에 문자를 덧붙이고  인덱스를 +1 한 후 재귀 호출

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 20 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 99.09 % of python3 submissions.
# Your memory usage beats 68.65 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
