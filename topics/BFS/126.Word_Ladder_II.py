from collections import deque
from typing import List
import string


"""
NOTE: This is the initial try, it gets time limit exceeded, im not very good yet.
I also tried bitmasks which was seriously stupid since 2^500 is a large number :) (This one got memory limit exceeded... i am truly special)
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = [beginWord] + wordList
        wordList = set(wordList)

        word_ind_map = {}
        for i, word in enumerate(wordList):
            word_ind_map[word] = i

        answer = []
        queue = deque([(beginWord, [beginWord])])
        visited = set(beginWord)
        while queue:
            (word, path) = queue.popleft()

            if word == endWord:
                if not answer:
                    answer.append(path)
                elif len(path) == len(answer[0]):
                    answer.append(path)
                else:
                    break

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1 :]
                    if new_word not in word_ind_map:
                        continue

                    if new_word in wordList and new_word not in visited:
                        queue.append((new_word, path + [new_word]))
                        visited.add(new_word)

        return answer


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
    answer = solution.findLadders(beginWord, endWord, wordList)
    print("answer: ", answer)
