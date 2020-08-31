# Design your implementation of the circular double-ended queue (deque).
#
# Your implementation should support following operations:
#
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return -1.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.
#
#
# Example:
#
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
# circularDeque.insertLast(1);			// return true
# circularDeque.insertLast(2);			// return true
# circularDeque.insertFront(3);			// return true
# circularDeque.insertFront(4);			// return false, the queue is full
# circularDeque.getRear();  			// return 2
# circularDeque.isFull();				// return true
# circularDeque.deleteLast();			// return true
# circularDeque.insertFront(4);			// return true
# circularDeque.getFront();			// return 4
#
#
# Note:
#
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Deque library.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k
        self.len = 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def _delete(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.len < 1:
            return False
        self.len -= 1
        self._delete(self.head)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.len < 1:
            return False
        self.len -= 1
        self._delete(self.tail.left.left)
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.len < 1:
            return -1
        return self.head.right.value

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.len < 1:
            return -1
        return self.tail.left.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.k == self.len


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# 51 / 51 test cases passed.
# Status: Accepted
# Runtime: 96 ms
# Memory Usage: 14.4 MB
#
# Your runtime beats 39.14 % of python3 submissions.
# Your memory usage beats 12.65 % of python3 submissions.
