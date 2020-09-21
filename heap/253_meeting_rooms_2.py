# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # algorithm
        # 1. sort the given meetings by their start time
        # 2. initialize a new min-heap and add the first meeting's ending time to the heap.
        # we simply need to keep track of the ending times as that tells us when a meeting room will get free
        # 3. for every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not
        # 4. if the room is free, then we extract the topmost element and add it back whith the ending time of the current meeting we are precessing.
        # 5. if not, then we allocate a new room and add it to the heap
        # 6. after processing all the meetings, the size of the heap will tell us the number of rooms allocated.
        # this will be the minimum number of rooms needed to accomodate all the meetings.

        # 예외 처리
        if not intervals:
            return 0

        # 자료 구조
        free_rooms = []  # min-heap

        # sort the meetings in increasing order of their start time.
        # 시작시간으로 정렬
        intervals.sort(key=lambda x: x[0])
        # add the first meeting. we have to five a new room to the first meeting.
        # heap에 가장 빠른 미팅시간의 ending time을 넣음
        heapq.heappush(free_rooms, intervals[0][1])

        # for all the remaining meeting rooms.
        for i in intervals[1:]:
            # if the room due to free up the earliest is free, assign that room to this meeting.

            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # if a new room is to be assigned, then also we add th the heap,
            # if and old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)

# 78 / 78 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Memory Usage: 17.1 MB
#
# Your runtime beats 89.42 % of python3 submissions.
# Your memory usage beats 54.38 % of python3 submissions.
#

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        # chronological order
        # two pointers  (start time pointer , end time pointer)

        if not intervals:
            return 0

        rooms = 0

        # separate out the start and the end timings and sort them individually.
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        length = len(intervals)

        # two pointers
        start_pointer = 0
        end_pointer = 0

        # until all the meetings have been processed
        while start_pointer < length:

            if end_times[end_pointer] <= start_times[start_pointer]:
                # free up a room and increment the end pointer.
                rooms -= 1
                end_pointer += 1

            rooms += 1
            start_pointer += 1

        return rooms


