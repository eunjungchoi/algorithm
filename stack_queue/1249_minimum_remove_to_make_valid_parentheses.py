# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
# so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.


class Solution:
    """
    '(', '') 및 소문자 영문자로 이루어진 문자열 s가 주어진다.

    괄호 문자열이 유효하도록 어느 위치에서든 최소한의 괄호 '(' 또는 ')'를 제거하고, 유효한 문자열을 반환하는 것이다.
    공식적으로 괄호 문자열은 다음과 같은 경우에만 유효하다.

    - 빈 문자열이며 소문자만 포함하거나
    - AB(B와 연결된 A)로 쓸 수 있으며, 여기서 A와 B는 유효한 문자열이다.
    - (A)라고 쓸 수 있는데, 여기서 A는 유효한 문자열이다.

    * 솔루션
    1. balance가 0일 때 마주치는 어떤 )도 제거해야 한다.
    2. )와 짝을 짓지 않는 (를 제거해야 한다. 문제가 있는 (의 인덱스를 알아야 한다. stack을 사용한다.
    (를 볼 때마다 스택에 추가한다. )를 볼 때마다 stack에서 (를 제거한다.
    ==> stack이 비어있을 때  )를 제거한다.
    ==> 최종 balance가 0이 아닌 경우, stack에서 인덱스를 제거한다.
    ( 지울 때 인덱스를 맨 뒤에서부터 앞으로 이동하면서 지우면  배열이 출렁거리지 않겠구나.
    근데 ) 지울 때는 어떻게 하지...  지울 인덱스 모아놨다가 뒤에서부터 지우면 되나.

    * 알고리즘
    1. 제거해야 하는 모든 인덱스를 식별
    2. 인덱스 제거 후 새 문자열 작성
    stack에 ( 인덱스 추가
    set에 unmatching ) 인덱스 추가

    시간 복잡도 : O(n)
    O(1)이 아닌 이유: string은 불변이기 때문에 수정 또는 삭제하려면 모든 문자열을 새로 생성해야 함.
    배열 중간에서 아이템 추가 삭제는 O(n). 공백을 메우기 위해 다른 아이템들이 움직여야 하기 때문에.
    바이너리 서치를 한다고 해도 O(logn)

    set에서 아이템을 찾는 것은 O(1)이다.
    """

    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''

        unmatched = set()
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    unmatched.add(i)
                else:
                    stack.pop()

        unmatched = unmatched.union(set(stack))
        return ''.join([char for i, char in enumerate(s) if i not in unmatched])


# 60 / 60 test cases passed.
# Status: Accepted
# Runtime: 108 ms
# Memory Usage: 16.2 MB
# #
# Your runtime beats 84.10 % of python3 submissions.
# Your memory usage beats 18.08 % of python3 submissions.
