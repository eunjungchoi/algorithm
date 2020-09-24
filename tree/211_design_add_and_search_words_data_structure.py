# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.


class WordDictionary:
    """
    새 단어를 추가할 수 있고,
    문자열이 이전에 추가된 문자열과 일치하는지 여부를 확인할 수 있는 데이터 구조를 설계하라
    단어 사전 클래서 구현
    - WordDictionary(): 객체를 초기화한다.
    - addWord(word): 데이터 구조에 단어를 추가하면, 나중에 매칭할 수 있다.
    - search(word): 데이터 구조에 단어와 일치하는 문자열이 있을 경우 true를 반환하거나, 그렇지 않으면 false를 반환한다. 단어들은 어떤 문자와도 일치시킬 수 있는  . 을 포함할 수 있다.

    """

    # Trie 구조
    # 트라이는 문자열을 사용한 효율적인 동적 추가/검색 작업에 주로 사용되는 검색 순서 트리 데이터 구조의 일종이다.
    # 자동 완성 검색, 철자 검사, T9 예측 테스트, IP 라우팅 (가장 긴 접두사 일치), 일부 GCC 컨테이너 등에 널리 사용된다.

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for char in word:
            if not char in node:
                node[char] = {}
            node = node[char]
            # node = node.setdefault(char, {})

        node['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        # DFS 탐색

        def search_in_node(word, node) -> bool:

            for i, char in enumerate(word):
                if not char in node:
                    if char == ".":
                        for child in node:
                            if child != '#' and search_in_node(word[i + 1:], node[child]):
                                return True
                    return False

                else:
                    node = node[char]

            return '#' in node

        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# 13 / 13 test cases passed.
# Status: Accepted
# Runtime: 320 ms
# Memory Usage: 24.4 MB
#
# Your runtime beats 75.32 % of python3 submissions.
# Your memory usage beats 67.79 % of python3 submissions.
