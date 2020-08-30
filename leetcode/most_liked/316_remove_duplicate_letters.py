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



