# Implement the RandomizedSet class:
#
# bool insert(int val) Inserts an item val into the set if not present.
# Returns true if the item was not present, false otherwise.
#
# bool remove(int val) Removes an item val from the set if present.
# Returns true if the item was present, false otherwise.
#
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is called).
# Each element must have the same probability of being returned.
#
# Follow up: Could you implement the functions of the class with each function works in average O(1) time?
#
#
#
# Example 1:
#
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
#
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
#
#
# Constraints:
#
# -231 <= val <= 231 - 1
# At most 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.
from random import choice


class RandomizedSet:
    """
    랜덤 집합 클래스 구현
    - insert(val) : 존재하지 않는 경우, set에 항목 val을 삽입한다. 항목이 없었으면 true를 반환하고, 아니면 false를 반환.
    - remove(val) : set에서 항목 val을 제거한다. (있는 경우).  항목이 있었으면 true를 반환, 없었으면 false를 반환
    - getRandom() : 현재 요소 집합에서 임의 요소를 반환한다. 호출 시 적어도 하나의 요소가 존재한다고 보장된다. 각 원소는 반환될 확률이 같아야 한다.
    - 추가: 각 기능 작업으로 클래스 기능을 평균 O(1) 시간 내에 구현할 수 있는가?
    """

    # 이 구조는 마르코프 체인 몬테카를로나, 메트로폴리스-헤이스팅스 알고리즘과 같은 대중적인 통계 알고리즘에 널리 사용된다.
    # 이런 알고리즘은 분포 자체를 계산하기 어려울 때 확률 분포로부터 표본을 추출하기 위한 것이다.

    # 구현 방법
    # 1)  해시맵: getRandom에 문제가 있지만, 평균 상수 시간에 insert, delete 수행 가능
    # 해시맵에는 인덱스가 없기 때문에 랜덤 값을 얻기 위해서는 먼저 리스트엣 해시맵 키를 변환해야 하며, 이는 선형적인 시간이 걸린다.
    # 해결책은 키 목록을 별도로 작성하고 이 목록을 사용해 일정 시간에 getRandom을 계산하는 것.
    # 2) Array list: 인덱스가 있으며 insert, getRandom을 평균 상수 시간에 제공 가능. 삭제에는 문제가 있음.
    # 임의의 인덱스에서 값을 삭제하려면 선형 시간이 걸린다. 여기서 해결책은 항상 마지막 값을 삭제하는 것이다.
    # - 마지막 요소와 삭제할 요소를 swap 한다
    # - 마지막 요소를 pop out 한다.
    # 이를 위해 일정한 시간에 각 요소의 인덱스를 계산해야 한다. 그러므로 element -> index 사전을 저장하는 해시맵이 필요하다.
    # 해시맵 (element: its index)
    # Array list

    # Approach 1: HashMap + ArrayList
    # - 딕셔너리에 value: index 형태로 추가.  O(1) time
    # - list에 index에 value 추가 O(1) time

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.dict:
            return False

        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        # 해시맵에서 삭제할 요소의 인덱스를 찾음.
        # 마지막 요소를 삭제할 요소의 위치로 이동. O(1)
        # 마지막 요소를 pop out.  O(1)

        if val in self.dict:
            # move the last element to the place index of the element to delete.
            last_val = self.list[-1]
            i = self.dict[val]
            self.dict[last_val], self.list[i] = i, last_val

            # delete the last element.
            self.list.pop()
            del self.dict[val]
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Memory Usage: 17.9 MB
#
# Your runtime beats 97.75 % of python3 submissions.
# Your memory usage beats 60.55 % of python3 submissions.
