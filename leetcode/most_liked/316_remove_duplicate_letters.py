# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Example 1:
#
# Input: "bcabc"
# Output: "abc"
# Example 2:
#
# Input: "cbacdcbc"
# Output: "acdb"

# by recursion
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 만들어 중복 없애고 정렬
        for i in sorted(set(s)):
            # 원래 string에서 인덱스를 찾아서 그 인덱스 부터의 뭉치들의 집합을 구함.
            suffix = s[s.index(i):]
            # 전체 집합과 접미사의 집합이 같으면 첫 문자를 분리해냄.
            if set(s) == set(suffix):
                new_s = suffix.replace(i, '')
                return i + self.removeDuplicateLetters(new_s)
        return ''


# 286 / 286 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 34.22 % of python3 submissions.
# Your memory usage beats 43.38 % of python3 submissions.


# by stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()  # 스택과 동일하게 저장함. 검색용.
        counter = collections.Counter(s)

        for i in s:
            counter[i] -= 1

            if i in seen:
                continue

            # 스택의 top과 비교해 현재 아이템이 top보다 앞서고, top의 개수가 아직 남아있으면  stack에서 top을 제
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(i)
            seen.add(i)

        return ''.join(stack)


# by stack:
# 286 / 286 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 92.15 % of python3 submissions.
# Your memory usage beats 48.15 % of python3 submissions.




