# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
# Constraints:
#
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
from collections import deque
from typing import List


class Solution:
    """
    2D board와 단어를 지정하면 그리드에 단어가 있는지 체크하라.
    단어는 순차적으로 인접한 셀의 문자로 구성될 수 있으며, 여기서 "인접" 셀은 수평 또는 수직으로 인접한 셀이다. 동일한 문자 셀은 두 번 이상 사용할 수 없다.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret

    def exist2(self, board: List[List[str]], word: str) -> bool:
        # DFS : 다음 방향을 시도하기 전에 가능한한 멀리 간다.
        # backtracking : 경로가 해결로 이어지지 않으면 그 변화를 다시 되돌림.  다른 경로를 시도.
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, words):
            if not words:
                return True

            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return False

            if board[i][j] != words[0]:
                return False

            board[i][j] = '#'
            for I, J in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:  # 동서남북 주변 셀 순회
                if dfs(I, J, words[1:]):
                    return True

            board[i][j] = word[0]
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word):
                    return True
        return False

    def exist3(self, board: List[List[str]], word: str) -> bool:
        queue = deque()

        def dfs(i, j, words, visited):
            if not words: return True
            if len(words) == 1 and board[i][j] == words[0]:
                return True
            if board[i][j] == words[0]:
                for I, J in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= I < len(board) and 0 <= J < len(board[0]) and (I, J) not in visited:
                        visited.add((I, J))
                        if dfs(I, J, words[1:], visited):
                            return True
                        visited.remove((I, J))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    queue.append([i, j])

        if not queue:
            return False

        if len(word) == 1:
            i, j = queue[0]
            return word == board[i][j]

        while queue:
            visited = set()
            i, j = queue.popleft()
            visited.add((i, j))
            if dfs(i, j, word, visited):
                return True
        return False


# time complexity:  O(N * 3^L) where N is the number of cells in the board and
# L is the length of the word to be matched.

# space complexity: O(L) where L is the length of the word.


# 89 / 89 test cases passed.
# Status: Accepted
# Runtime: 332 ms
# Memory Usage: 15.8 MB
#
# Your runtime beats 84.58 % of python3 submissions.
# Your memory usage beats 11.97 % of python3 submissions.

