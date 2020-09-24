# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.
#
# addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.
#
#
#
# Example:
#
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
#
# Output:
# [null,[],null,null,["a"],"hello"]
#
# Explanation:
# filesystem
#
#
# Note:
#
# You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
# You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.

from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""


class FileSystem:
    """
    다음 기능들을 위해 메모리 내 파일 시스템을 설계하라.

    ls: 문자열 형식의 경로 지정. 파일 경로인 경우 이 파일 이름만 포함된 목록을 반환하라. 디렉터리 경로인 경우, 이 디렉터리의 파일 및 디렉터리 이름 목록을 반환하라. 출력물은 사전순으로 작성되어야 한다.

    mkdir: 존재하지 않는 디렉토리 경로가 주어진 경우, 경로에 따라 새로운 디렉터리를 만들어야 한다. 경로의 중간 디렉터리도 존재하지 않는 경우, 해당 디렉터리도 생성하라.

    addContentToFile: 문자열 형식의 파일 경로 및 파일 컨텐츠가 주어진다. 파일이 없으면 지정된 내용을 포함하는 파일을 만들어야 한다. 파일이 이미 있는 경우, 기존 내용에 지정된 내용을 추가하라.

    readContentFromFile: 파일 경로가 지정되면 해당 콘텐츠를 문자열 형식으로 반환하라.
    """

    # approach 1: trie

    def __init__(self):
        self.root = Node()

    def find(self, path):  # find and return node at path.
        curr = self.root
        if len(path) == 1:  # '/' 일 때,
            return self.root

        for word in path.split("/")[1:]:
            curr = curr.child[word]

        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.find(path)

        if curr.content:  # file path, return file name
            return [path.split('/')[-1]]

        return sorted(curr.child.keys())  # directory일 때.

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
#
# 63 / 63 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 14.1 MB

# Your runtime beats 69.36 % of python3 submissions.
# Your memory usage beats 40.24 % of python3 submissions.
