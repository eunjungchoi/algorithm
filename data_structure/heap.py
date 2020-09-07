# python 에서는 최소 힙 (min heap)만 구현되어 있음.
# 최소 힙은 부모가 항상 자식보다 작기 때문에 후트가 결국 가장 작은 값을 갖게 되며,
# 우선순위 큐에서 가장 작은 값을 추출하는 것은 매번 힙의 루트를 가져오는 형태.
# 우선순위 큐 ADT 는 주로 힙으로 구현하고, 힙은 주로 배열로 구현.

# 힙은 정렬된 구조가 아님.
# 최소 힙의 경우 부모 노드가 가장 작다는 조건만 만족할 뿐, 서로 정렬되어 있지 않음.

# 힙 정렬 알고리즘을 고안하면서 설계됨.
# 완전 이진 트리 형태인 이진 힙은 배열에 빈틈없이 배치가 가능함.
# 항상 균형을 유지하는 특징 때문에 힙은 다양한 분야에 널리 활용됨
# 우선순위 큐, 다익스트라 알고리즘.
# 힙 정렬,
# 최소 신장 트리를 구현하는 프림 알고리즘
# 중앙값의 근사값을 빠르게 구하는 데도 활용됨.


class BinaryHeap(object):
    def __init__(self):
        self.items = [None]  # 0번 인덱스는 사용하지 않음

    def __len__(self):
        return len(self.items) - 1

# 삽입 (up-heap)
# 1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입 (배열로 표현할 경우, 가장 마지막에 삽입함)
# 2. 부모 값과 비교해 값이 더 작은 경우 위치를 스왑한다.
# 3. 계속해서 부모 값과 비교해 위치를 스왑한다.  ( 가장 작은 값일 경우 루트까지 올라감)

    def _percolate_up(self):   # 내부 함수라는 의미. _를 붙임.
        i = len(self)
        parent = i // 2

        while parent >= 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]

            i = parent
            parent = i // 2

        # 시간복잡도 = O(log n)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
        # 기존 파이썬 heap 모듈의 heapq.heappush() 가 여기에 대응.

# 추출
# 루트를 추출하면 됨
# 추출 이후에 비어있는 루트에는 가장 마지막 요소가 올라감
# 이제 반대로 자식 노드와 값을 비교해서 자식보다 크다면 내려가는 다운힙 down-heap 연산이 수행

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
        # heapq.heappop()이 여기에 대응.
