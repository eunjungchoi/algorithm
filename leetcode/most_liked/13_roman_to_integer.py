# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    @staticmethod
    def roman_to_int(self, s: str) -> int:
        result: int = 0
        key: int = 0
        last: int = len(s) - 1

        while key <= last:
            if s[key] == 'I':
                if key + 1 <= last and s[key + 1] == 'V':
                    result += 4
                    key += 1
                elif key + 1 <= last and s[key + 1] == 'X':
                    result += 9
                    key += 1
                else:
                    result += 1
            elif s[key] == 'V':
                result += 5
            elif s[key] == 'X':
                if key + 1 <= last and s[key + 1] == 'L':
                    result += 40
                    key += 1
                elif key + 1 <= last and s[key + 1] == 'C':
                    result += 90
                    key += 1
                else:
                    result += 10
            elif s[key] == 'L':
                result += 50
            elif s[key] == 'C':
                if key + 1 <= last and s[key + 1] == 'D':
                    result += 400
                    key += 1
                elif key + 1 <= last and s[key + 1] == 'M':
                    result += 900
                    key += 1
                else:
                    result += 100
            elif s[key] == 'D':
                result += 500
            elif s[key] == 'M':
                result += 1000

            key += 1

        return result






