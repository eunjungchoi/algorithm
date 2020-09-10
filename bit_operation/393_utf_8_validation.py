# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
#
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:
#
#    Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#    --------------------+---------------------------------------------
#    0000 0000-0000 007F | 0xxxxxxx
#    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
#
# Note:
# The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.
#
# Example 1:
#
# data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.
#
# Return true.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
# Example 2:
#
# data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.
#
# Return false.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is invalid.

# 입력값이 UTF-8이 맞는지 검증하라
# ex) 첫 바이트가 1110 으로 시작한다면 3바이트 문자. 뒤 따르는 2바이트는 모두 10으로 시작해야 유효한 uTF-8 문자가 됨.
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        # 사이즈를 파라미터로 받아 해당 사이즈만큼만 바이트가 10으로 시작하는지를 판별
        # 즉, 앞서 첫 바이트 기준으로 3바이트 문자라고 판별했다면, 나머지 2바이트가 모두 10으로 시작하는지 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]  # 첫 바이트 기준 총 문자 바이트 판별

            # 첫 바이트 변수가 0으로 시작한다면 1바이트 문자
            # 110으로 시작한다면 2바이트 문자
            # 1110 으로 시작한다면 3바이트 문자
            # 11110 으로 시작한다면 4바이트 문자로 판별

            # and 이후에는 각각 해당 바이트의 문자가 맞는지를 check() 함수로 판별

            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False

        return True


# 49 / 49 test cases passed.
# Status: Accepted
# Runtime: 112 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 87.19 % of python3 submissions.
# Your memory usage beats 94.11 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고
