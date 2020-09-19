# Median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
#
#
# Example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
#
# Follow up:
#
# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # heap 두개를 준비. 하나는 small, large
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps

        item = heapq.heappushpop(large, num)  # large 그룹 heap에  num을 넣고 제일 작은 값을 추룰
        heapq.heappush(small, -item)
        # 파이썬은 최소힙이기 때문에 small 그룹의 heap에서 최대값을 뽑아내려면 - 음수로 바꾸어서 넣어줌.
        # 최대값이 최소값이 되기 때문에 최솟값 추출 가능

        if len(small) > len(large):
            heapq.heappush(large, -heapq.heappop(small))  # small 그룹이 더 개수가 많으면 최대값을 뽑아서 부호를 양수로 바꿔서 large 그룹에 넣어줌.

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(small) < len(large):
            return float(large[0])

        return (-small[0] + large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 188 ms
# Memory Usage: 25.2 MB
#
# Your runtime beats 97.51 % of python3 submissions.
# Your memory usage beats 20.01 % of python3 submissions.
