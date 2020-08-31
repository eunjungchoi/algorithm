# Design your implementation of the circular queue.
# The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out)
# principle and the last position is connected back to the first position to make a circle.
# It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.
#
# Your implementation should support following operations:
#
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p1] is not None:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.p1 == self.p2 and self.q[self.p1] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 94.21 % of python3 submissions.
# Your memory usage beats 50.33 % of python3 submissions.
