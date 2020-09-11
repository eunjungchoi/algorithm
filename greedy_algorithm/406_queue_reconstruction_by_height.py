# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


# 여러 명의 사람들이 줄을 서 있다. 각각의 사람은 (h, k) 의 두 정수 쌍을 갖는데,
# h는 그 사람의 키, k는 앞서 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수를 뜻한다.
# 이 값이 올바르도록 줄을 재정렬하는 알고리즘을 작성하라.

# 우선순위 큐 이용.
# 우선순위 큐 자체가 매번 그때그때의 최소 또는 최댓값을 추출하기 때문에, 그리디에 어울리는 대표적인 자료구조.
# 그리디 문제의 대부분은 우선순위 큐를 활용해 풀이한다.
import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # 첫번째 값이 큰 순서대로 추출되는 최대 힙 (max heap) 형태로 풀이 가능.
        # 두번째 값은, 삽입되는 인덱스로 활용
        # 파이썬은 최소 힙 min heap 만 지원하기 때문에, 첫 번째 값을 음수로 변경해 최소 힙에서도 최대 힙처럼 구현

        heap = []

        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []

        # 키 역순, 인덱스 추출

        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result


# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 104 ms
# Memory Usage: 14.5 MB
#
# Your runtime beats 67.46 % of python3 submissions.
# Your memory usage beats 21.72 % of python3 submissions.
