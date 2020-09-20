# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 예외 처리
        if numRows == 1:
            return s
        if numRows > len(s):
            return s

        # 자료 구조
        L = [''] * numRows
        index = 0
        direction = 1

        for char in s:
            L[index] += char

            if index == 0:    # 글자가 아래로 내려갈때 L에서 다음 인덱스 (=다음줄)로 넘어가도록 step을 1로 설정.  밑에서 index += step 해줌.
                direction = 1
            elif index == numRows - 1:
                # 인덱스가  제일 마지막 줄에 도달하면 이제 거꾸로 위로 올라가면서 글자를 써야 함 . 그래서 index를 -1로 줄여가며  글자를 덧붙여야 함.
                direction = -1

            index += direction

        return ''.join(L)


# 1158 / 1158 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 13.7 MB
#
# Your runtime beats 98.99 % of python3 submissions.
# Your memory usage beats 88.96 % of python3 submissions.
