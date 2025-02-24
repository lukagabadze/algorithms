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

NOTE: I have now improved the time limit complexity significantly by keeping the depth_map and, adding the answers matrix and also adding visited set.
You can read what they are for in the comments below.
But the solution is still not complete, I am getting MLE since I am storing all shortest paths for every word in the answers matrix.
If I can fix that, I am confident this will be a successful submission!
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        # Queue holds the word we are currently on and the steps it took to reach it.
        queue = deque([(beginWord, 1)])

        # answers matrix holds minimum path arrays for every word.
        # answers[word] is an array with all the possible shortest ways you can reach word from beginWord.
        answers = {word: [] for word in wordList}
        answers[beginWord] = [[beginWord]]
        answers[endWord] = []

        # depth_map dictionary holds how many steps it takes to reach a certain word
        # before appending a word to the queue you can check if he have already reached this word in less steps.
        # depth_map[word] holds a number indicating shortest amount of steps it takes to reach that word.
        depth_map = {word: float("inf") for word in wordList}
        depth_map[beginWord] = 1
        depth_map[endWord] = float("inf")

        # This set holds words which were already processed,
        # all the neighbours have been checked and added to the queue if necessary.
        # There is no need to revisit that word again.
        # NOTE: I always had visited.add(...) next to the queue.append logic,
        # but in this case, we have to append all the nodes first and THEN mark the word as visited.
        visited = set()
        while queue:
            (word, steps) = queue.popleft()

            if word in visited:
                continue

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i + 1 :]

                    if new_word == word or new_word not in wordList:
                        continue

                    if steps + 1 <= depth_map[new_word]:
                        queue.append((new_word, steps + 1))
                        answers[new_word].extend(
                            path + [new_word] for path in answers[word]
                        )
                        depth_map[new_word] = steps + 1

            visited.add(word)

        return answers[endWord]


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

    # beginWord = "red"
    # endWord = "tax"
    # wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]

    print("beginWord: ", beginWord)
    print("endWord: ", endWord)
    print("wordList: ", wordList)
    print("\n")
    answer = solution.findLadders(beginWord, endWord, wordList)
    print("answer: ", answer)
