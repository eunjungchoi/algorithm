# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

# m x n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라.
# 행렬은 왼쪽에서 오른쪽, 위에서 아래로 오름차순으로 정렬되어 있다.


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 첫 행의 맨 뒤 요소를 택한 다음, 타겟이 이보다 작으면 왼쪽으로, 크ㅕㄴ 아래로 이동하게 하는 방법이다.
        # 행렬은 왼쪽에서 오른쪽으로, 위에서 아래로 오름차순으로 정렬되어 있기 때문에.

        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True

            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1

            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1

        return False

        # pythonic way
        # return any(target in row for row in matrix)


# 129 / 129 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 18.5 MB
#
# Your runtime beats 99.50 % of python3 submissions.
# Your memory usage beats 56.51 % of python3 submissions.

