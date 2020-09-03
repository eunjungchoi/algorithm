# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Example:
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format,
# so please be creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']

        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()

            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Runtime: 104 ms, faster than 98.72% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 18.3 MB, less than 81.77% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# <파이썬 알고리즘 인터뷰> 참고.
