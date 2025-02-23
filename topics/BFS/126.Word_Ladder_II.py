from collections import deque
from typing import List
import string


"""
NOTE: This is the initial try, it gets time limit exceeded, im not very good yet.
I also tried bitmasks which was seriously stupid since 2^500 is a large number :) (This one got memory limit exceeded... i am truly special)

NOTE: I peeked into the solutions tab and found one solution which mentioned depthMap,
so I switched back to the editor immediately and wrote a depth_map solution,
I still get TLE, but on the 53rd case (there are 57 in total).
So it is better, but still not good enough.
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        cnt = 0
        answer = []
        queue = deque([(beginWord, [beginWord])])
        depth_map = {word: float("inf") for word in wordList}
        depth_map[beginWord] = 1
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

                    if new_word not in wordList:
                        continue

                    if len(path) + 1 <= depth_map[new_word]:
                        queue.append((new_word, path + [new_word]))
                        depth_map[new_word] = len(path) + 1
                        cnt += 1

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
