# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
from typing import List


class Solution:
    """
    정렬되지 않은 정수 배열이 주어진다. 가장 긴 증가 수열의 길이를 찾아라.

    the idea extends to:
    initial sub = [ ].
    traversing the nums:

    a) if val > sub's all elements, then subsequence length increased by 1, sub.append(val);
    b) if sub[i-1] < val < sub[i], then we find a smaller value, update sub[i] = val. Some of the elements stored in the sub[ ] are known subsequences, and the other part is elements of other possible new subsequences. However, the length of the known subsequences is unchanged.
    return the sub[ ]'s length.

    Here is the solution's track, as we have nums = [8, 2, 5, 1, 6, 7, 9, 3],when we traversing the nums:

    i = 0,    sub = [8]
    i = 1,    sub = [2]
    i = 2,    sub = [2, 5]
    i = 3,    sub = [1, 5],    # element has been changed, but the sub's length has not changed.
    i = 4,    sub = [1, 5, 6]
    i = 5,    sub = [1, 5, 6, 7]
    i = 6,    sub = [1, 5, 6, 7, 9]
    i = 7,    sub = [1, 3, 6, 7, 9]    #done! Although the elements are not correct, but the length is correct.
    """

    # O(n*m) solution. m is the sub[]'s length
    def lengthOfLIS(self, nums):
        sub = []
        for val in nums:
            pos, sub_len = 0, len(sub)
            while pos <= sub_len:  # update the element to the correct position of the sub.
                if pos == sub_len:
                    sub.append(val)
                    break
                elif val <= sub[pos]:
                    sub[pos] = val
                    break
                else:
                    pos += 1

        return len(sub)

    # Because of sub[ ] is incremental, we can use a binary search to find the correct insertion position.

    # O(nlogn) solution with binary search
    def lengthOfLIS2(self, nums: List[int]) -> int:

        def binarySearch(sub, val):
            lo, hi = 0, len(sub) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo

        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)

