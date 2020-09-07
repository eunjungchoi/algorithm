
# 트라이 Trie 는 실무에 매우 유용하게 쓰이는 자료구조로서, 특히 자연어 처리 (NLP) 분야에서 문자열 탐색을 위한 자료구조로 널리 쓰인다.
# 검색을 뜻하는 retrieval 의 중간 음절에서 용어를 따왔다.
# 트리는 트리와 유사하지만, 이진 트리의 모습이 아닌, 전형적인 다진 m-ary Tree의 형태를 띈다.
# 각각의 문자 단위로 색인을 구축한 것과 유사하다.
# 문자열의 길이만큼만 탐색하면 된다.
# 자연어 처리 분야에서는 형태소 분석기에서 분석 패턴을 트라이로 만들어두고 자연어 문장에 대해 패턴을 찾아 처리하는 등으로 활용하고 있다.


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.children
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['#'] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.children

        for char in word:
            if char not in current:
                return False
            current = current[char]
        return '#' in current

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.children
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 132 ms
# Memory Usage: 27.1 MB
#
# Your runtime beats 95.69 % of python3 submissions.
# Your memory usage beats 89.56 % of python3 submissions.
