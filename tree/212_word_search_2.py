# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
#
#
# Example:
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
# Note:
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
import collections
from typing import List


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)

        if not node:
            return

        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp

    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:

        WORD_KEY = '$'
        trie = {}

        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})  # 주어진 key에 대한 value를 반환. nested 하게 계속 들어가는 구조.
            node[WORD_KEY] = word

        rows = len(board)
        cols = len(board[0])

        matched_words = []

        def backtracking(row, col, parent):
            char = board[row][col]
            curr_node = parent[char]

            word_match = curr_node.pop(WORD_KEY, False)
            if word_match:
                matched_words.append(word_match)

            # mark the cell as visited
            board[row][col] = '#'
            for (r, c) in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue

                if board[r][c] not in curr_node:
                    continue

                backtracking(r, c, curr_node)

            # restore the cell
            board[row][col] = char

            if not curr_node:
                parent.pop(char)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched_words


# 36 / 36 test cases passed.
# Status: Accepted
# Runtime: 204 ms
# Memory Usage: 28.2 MB
#
# Your memory usage beats 74.77 % of python3 submissions.
# Your runtime beats 99.38 % of python3 submissions.
