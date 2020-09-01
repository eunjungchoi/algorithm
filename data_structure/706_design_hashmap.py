# Design a HashMap without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# put(key, value) : Insert a (key, value) pair into the HashMap.
# If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
#
# Example:
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)
#
# Note:
#
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size

        if self.table[index].value is None:  # 존재하지 않는 인덱스로 조회하면 그 자리에서 바로 디폴트 객체인 빈 listNode를 생성
            self.table[index] = ListNode(key, value)
            return
        else:
            node = self.table[index]
            while node:
                if node.key == key:  # 키가 같으면 값을 업데이트
                    node.value = value
                    return
                if node.next is None:
                    break
                node = node.next  # 키가 다르고 다음 노드가 있으면, 계속 다음 노드로 이동

            node.next = ListNode(key, value)  # 다음 노드가 없으면 그 자리에 새 리스트노드 생성

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size

        if self.table[index].value is None:
            return -1

        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size

        if self.table[index].value is None:
            return

        node = self.table[index]
        # 인덱스의 첫 번째 노드일 때 바로 삭제
        if node.key == key:
            self.table[index] = ListNode() if node.next is None else node.next
            return

        # 연결리스트 노드 삭제
        prev = node
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev, node = node, node.next

        # n = prev.next.next
        # prev.next = n


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 33 / 33 test cases passed.
# Status: Accepted
# Runtime: 232 ms
# Memory Usage: 16.9 MB
#
# Your runtime beats 81.92 % of python3 submissions.
# Your memory usage beats 58.41 % of python3 submissions.
