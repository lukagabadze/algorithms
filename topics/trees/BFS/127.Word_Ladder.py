from collections import deque
from typing import List
import string


"""
Method 1:
TIME: 8497ms (Beats 5.00%)
NOTE: Improve the solution this result is just disgusting

Method 2:
TIME: 334ms (Beats 36.63%)
NOTE: Much better! In this method, you don't go through the each word in wordList every iteration.
Instead, you assemble the new word by changing out each character by a new one since `beginWord, endWord, and wordList[i] consist of lowercase English letters`.
HUGE Thanks to Himanshu Malik for the solution! (https://leetcode.com/problems/word-ladder/solutions/1764371/a-very-highly-detailed-explanation/)
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            (word, ans) = queue.popleft()

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1 :]
                    if new_word not in visited and new_word in wordList:
                        visited.add(new_word)
                        queue.append((new_word, ans + 1))
                        if new_word == endWord:
                            return ans + 1

        return 0


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
