# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given a 2D char matrix representing the game board.
# 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,
# digit ('1' to '8') represents how many mines are adjacent to this revealed square,
# and finally 'X' represents a revealed mine.
#
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
# return the board after revealing this position according to the following rules:
#
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed,
# then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed,
# then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
#
#
# Example 1:
#
# Input:
#
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
#
# Click : [3,0]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Example 2:
#
# Input:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Click : [1,2]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
#
#
# Note:
#
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'),
# which also means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been revealed).
# For simplicity, not mentioned rules should be ignored in this problem.
# For example, you don't need to reveal all the unrevealed mines when the game is over,
# consider any cases that you will win the game or flag any squares.
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # DFS 깊이 우선 탐색으로 풀이
        # 클릭 위치가 M일 때: X로 바꾸고 return
        # 클릭 위치가 E일 때: 동서남북+대각선 8개 위치를 탐색 후 mine 개수 세기
        # mine 개수가 1 이상이면 board[i][j] = mine 숫자값 표기
        # 0이면 'B'로 표기
        # 주변 8개 위치를 dfs에 재귀호출
        # board 반환

        # 예외 처리
        if not board or not board[0]:
            return []

        # 자료 구조
        # rows, cols = len(board), len(board[0])
        i, j = click[0], click[1]

        # 클릭 포지션이 M이면 X로 바꾸고 return  (game is over)
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs(board, i, j)
        return board

    def dfs(self, board, i, j):
        if board[i][j] != 'E':
            return

        directions = [(i + 1, j + 1), (i, j + 1), (i - 1, j + 1), (i + 1, j), (i - 1, j), (i + 1, j - 1), (i, j - 1),
                      (i - 1, j - 1)]

        mine_count = 0
        for I, J in directions:
            if 0 <= I < len(board) and 0 <= J < len(board[0]) and board[I][J] == 'M':
                mine_count += 1

        board[i][j] = mine_count
        if mine_count:
            board[i][j] = str(mine_count)
            return
        else:
            board[i][j] = 'B'

        for I, J in directions:
            if 0 <= I < len(board) and 0 <= J < len(board[0]):
                self.dfs(board, I, J)


# 54 / 54 test cases passed.
# Status: Accepted
# Runtime: 188 ms
# Memory Usage: 17.3 MB
#
# Your runtime beats 91.46 % of python3 submissions.
# Your memory usage beats 16.22 % of python3 submissions.
