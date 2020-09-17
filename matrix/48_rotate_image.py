# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Example 3:
#
# Input: matrix = [[1]]
# Output: [[1]]
# Example 4:
#
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
#
#
# Constraints:
#
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #  * clockwise rotate
        #  * first reverse up to down, then swap the symmetry
        #  * 1 2 3     7 8 9     7 4 1
        #  * 4 5 6  => 4 5 6  => 8 5 2
        #  * 7 8 9     1 2 3     9 6 3

        # 1. 위아래 순서를 바꿈. A.reverse() or A[::-1]
        matrix.reverse()

        # 2. 대칭 변환
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#  * anticlockwise rotate
#  * first reverse left to right, then swap the symmetry
#  * 1 2 3     3 2 1     3 6 9
#  * 4 5 6  => 6 5 4  => 2 5 8
#  * 7 8 9     9 8 7     1 4 7
# */
# void anti_rotate(vector<vector<int> > &matrix) {
#     for (auto vi : matrix) reverse(vi.begin(), vi.end());
#     for (int i = 0; i < matrix.size(); ++i) {
#         for (int j = i + 1; j < matrix[i].size(); ++j)
#             swap(matrix[i][j], matrix[j][i]);
#     }
# }

# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 86.30 % of python3 submissions.
# Your memory usage beats 47.66 % of python3 submissions.
