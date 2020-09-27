# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List


class Solution:
    # m x n 행렬이 주어질 때, 행렬의 모든 원소를 나선형 순서로 반환하라.
    # Here's how the matrix changes by always extracting the first row and
    # rotating the remaining matrix counter-clockwise:

    #     |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    #     |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    #     |7 8 9|      |4 7|
    # Now look at the first rows we extracted:

    #     |1 2 3|      |6 9|      |8 7|      |4|      |5|
    # Those concatenated are the desired result.

    # Another visualization
    #   spiral_order([[1, 2, 3],
    #                 [4, 5, 6],
    #                 [7, 8, 9]])

    # = [1, 2, 3] + spiral_order([[6, 9],
    #                             [5, 8],
    #                             [4, 7]])

    # = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
    #                                      [5, 4]])

    # = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
    #                                               [5]])

    # = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

    # = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

    # = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

    # = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        # zip이 이터레이터를 리턴. 리스트로 만들어줘야 함.  리스트를 만들 때는 * 이걸 써서 하나씩 풀어준다음에 list로 싸기
        return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])



# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 79.31 % of python3 submissions.

