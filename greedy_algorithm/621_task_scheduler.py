# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
#
#
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
# Constraints:
#
# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].

# A에서 Z로 표현된 태스크가 있다. 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고, n번의 간격 내에는 동일한 태스크를 실행할 수 없다.
# 더 이상 태스크를 실행할 수 없는 경우 idle 상태가 된다. 모든 태스크를 실행하기 위한 최소 간격을 출력하라.
# 우선순위 큐를 이용해 그리디하게 풀 수 있는 문제

import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # 아이템을 추출한 다음에는 매번 아이템 개수를 업데이트해줘야 함
        # 우선순위 큐를 사용해 가장 개수가 많은 아이템부터 하나씩 추출해야 하는데, 문제는 전체를 추출하는 게 아니라 하나만 추출하고 빠진 개수를 업데이트 할 수 있는 구조가 필요함.

        # 1. 만약 heapq를 사용한다면 다음과 같은 형태

        # for task, count in collections.Counter(task).items():
        #     heapq.heaqpush(heap, (-count, task))
        #     count, task = heapq.heappop(heap)
        #     heapq.heappush(heap, (-count+1, task))

        # 각 태스크의 개수를 Counter로 계산하고 이 값을 힙에 추가한다. heapq는 최소 힙만을 지원하기 때문에 최대 힙 효과를 내기 위해 음수로 변환하여 저장한다.
        # heappop()은 항목 전체가 추출되기 때문에 꺼내서 활용한 이후에는 heappush로 개수를 줄여 다시 추가하는 작업이 필요하다. (여기서는 음수이기 때문에 +1을 하여. )

        # 2. 이런 번거로운 작업을 Counter 만으로 간결하게 처리할 수 있다. counter.subtract
        # most_common은 가장 개수가 많은 아이템부터 출력하는 함수. 사실상 최대 힙과 같은 역할
        # pop()으로 추출되는 것은 아니기 때문에 subtract(task)를 지정해서 1개씩 개수를 별로도 줄여나감.
        # 빈 Counter()를 더하면 0 이하인 아이템은 목록에서 아예 삭제하는 기능이 있음.

        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0

            # 개수 순 추출
            # n+1을 쓰는 것이 트릭
            # n+1개가 추출될 때는 idle 없이 실행함. 입력값이 n=2 였기 때문에 n+1을 추출했을 때 3개가 모두 나온다면 idle 없이 계속 진행함.
            # 2개만 추출되면 한번 idle하고 마지막으로 A를 출력.

            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)

                # 0 이하인 아이템을 목록에서 완전히 제거.
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result


# 71 / 71 test cases passed.
# Status: Accepted
# Runtime: 1256 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 5.06 % of python3 submissions.
# Your memory usage beats 12.05 % of python3 submissions.
