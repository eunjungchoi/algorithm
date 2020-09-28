# We are given a list schedule of employees, which represents the working time for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
#
# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
#
# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
#
#
#
# Example 1:
#
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:
#
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
#
#
# Constraints:
#
# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8


"""
각 직원들의 근무 시간을 나타내는 직원들의 리스트 schedule을 받는다.
각 직원마다 겹치지 않는 인터벌 목록이 있으며, 이 인터벌은 정렬된 순서로 되어 있다.

모든 직원이 공통으로 쉬는, 양의 길이의 자유시간을 나타내는, 유한한 인터벌의 리스트를 정렬된 순서로 반환하라.

간격을 [x, y]로 표시하지만, 내부 객체는 리스트나 배열이 아닌 인터벌 들이다.
"""


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end



class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        간격은 어느 직원의 것인지는 중요하지 않으니, 그냥 평평하게 한다.
        """

        times = [time for s in schedule for time in s]
        times = sorted(times, key=lambda x: x.start)
        result = []
        pre = times[0]
        for time in times[1:]:
            if time.start <= pre.end < time.end:
                pre.end = time.end
            elif time.start > pre.end:
                result.append(Interval(pre.end, time.start))
                pre = time

        return result


# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 15.8 MB
#
# Your runtime beats 100.00 % of python3 submissions.

