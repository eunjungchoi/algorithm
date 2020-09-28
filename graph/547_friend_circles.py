# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
#
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
#
# Example 2:
#
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
#
#
#
# Constraints:
#
# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]
from typing import List


class Solution:
    """
    한 학급에는 N명의 학생이 있다. 그들 중 몇몇은 친구인 반면, 몇몇은 그렇지 않다. 그들의 우정은 천성적으로 전이적이다. 예를 들어 A가 B의 직접적인 친구고 B가 C의 직접적인 친구라면 A는 C의 간접적인 친구다. 그리고 우리는 프렌드 서클이 직접적이거나 간접적인 친구인 학생들의 그룹이라고 정의했다.

반 학생들 간의 친구 관계를 나타내는 N*N 매트릭스 M을 부여한다. M[i][j]이 1이면 ith와 jth 학생들은 서로 직접적인 친구이고, 0이면 그렇지 않다.

모든 학생 중에서 친구 서클의 총 개수를 출력하라.

# 연결된 그래프의 개수 구하기

    """

    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()

        def dfs(node):
            for neighbor, is_connected in enumerate(M[node]):
                if is_connected and neighbor not in visited:  # 친구이고, 그 친구가 아직 방문 안한 상태일 때만 깊이탐색.
                    visited.add(neighbor)
                    dfs(neighbor)

        num_of_circle: int = 0

        for i in range(len(M)):  # num_of_student. 한명씩 돌아가면서. 순회.
            if i not in visited:  # 다른 친구를 통해 추가됐으면 pass. 새로 시작하면 그룹 +1
                dfs(i)
                num_of_circle += 1

        return num_of_circle


# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 172 ms
# Memory Usage: 14.7 MB
#
# Your runtime beats 99.90 % of python3 submissions.
# Your memory usage beats 11.04 % of python3 submissions.
