
# 전위 순회 pre-Order (NLR)
# 중위 순회 In-Order (LNR)
# 후위 순회 post-Order (LRN)


# N: 현재 노드 자신
# L: 현재 노드의 왼쪽 서브트리
# R: 현재 노드의 오른쪽 서브트리


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node('F',
            Node('B',
                 Node('A'),
                 Node('D',
                      Node('C'), Node('E'))
                 ),
            Node('G',
                 None,
                 Node('I', Node('H'))
                 )
            )


# 전위 순회

def preorder(node):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


preorder(root)


# 중위 순회


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)


inorder(root)


# 후위 순회

def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val)


postorder(root)
