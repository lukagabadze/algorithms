from collections import deque
from typing import List


"""
TIME: 8497ms (Beats 5.00%)
NOTE: Improve the solution this result is just disgusting
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            (currentWord, ans) = queue.popleft()

            for word in wordList:
                if word not in visited:
                    if self.two_words_diff(currentWord, word) == 1:
                        visited.add(word)
                        queue.append((word, ans + 1))

                        if word == endWord:
                            return ans + 1

        return 0

    def two_words_diff(self, word1: str, word2: str) -> int:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1

        return diff


if __name__ == "__main__":
    solution = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]

    # beginWord = "leet"
    # endWord = "code"
    # wordList = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]

    print("beginWord: ", beginWord)
    print("endWord: ", endWord)
    print("wordList: ", wordList)
    print("\n")
    answer = solution.ladderLength(beginWord, endWord, wordList)
    print("answer: ", answer)
