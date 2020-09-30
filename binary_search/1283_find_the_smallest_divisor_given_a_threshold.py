# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
#
# Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
#
# It is guaranteed that there will be an answer.
#
#
#
# Example 1:
#
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
# Example 2:
#
# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3
# Example 3:
#
# Input: nums = [19], threshold = 5
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6
from typing import List


class Solution:
    """
    정수의 배열과 정수 임계값을 지정하면 양의 정수 구분자를 선택하고 그 배열을 모두 그 배열에 따라 나누어 분할 결과를 합산한다. 위에서 언급한 결과가 임계값보다 작거나 같도록 가장 작은 구분자를 찾으십시오.

    분할의 각 결과는 해당 요소보다 크거나 같은 가장 가까운 정수로 반올림된다(예: 7/3 = 3 및 10/2 = 5).

    반드시 답이 있을 것이다.


    *** Binary search the result.
    If the sum > threshold, the divisor is too small.
    If the sum <= threshold, the divisor is big enough.

    *** Complexity
    Time O(NlogM), where M = max(nums)
    Space O(1)

    """

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)  # 주어진 리스트에서 가장 큰 숫자가 right 바운더리

        while left < right:
            middle = (left + right) // 2
            # if sum( math.ceil(num / middle) for num in nums) > threshold:
            if sum((num + middle - 1) // middle for num in nums) > threshold:
                left = middle + 1  # divisor를 좀 더 크게 해야 함.
            else:  # sum  <= threshold.  divisor is big enough.  왼쪽 탐색.
                right = middle

        return left


# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 348 ms
# Memory Usage: 19.9 MB
#
# Your runtime beats 98.24 % of python3 submissions.
# Your memory usage beats 11.90 % of python3 submissions.
