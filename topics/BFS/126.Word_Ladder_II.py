from collections import deque, defaultdict
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

NOTE: defaultdict is pretty cool.
It initializes the dictionary with default values. `defaultdict(list)` will have an empty array for every unassigned key.
You can also put lambda in it, `defaultdict(lambda: float("inf"))` here, every uninitialized key will have a float("inf") value.

NOTE: I finally got the code accepteeeddd no TLE or MLE 😭😭😭😭😭😭.
Last issue I had was MLE, because I was storing every shortest path for every word in a matrix called answers.
Instead of doing that, you can create a parents dictionary which will hold set of parent words for every word.
Then you can use a simple backtrack function to assemble the arrays.
Thank you to ChatGPT for helping me out on this one.

NOTE: There is a way to speed this up using Bidirectional BFS but I think that would be a topic for another day.
TODO: Implement Bidirectional BFS.
"""


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        # Queue holds the word we are currently on and the steps it took to reach it.
        queue = deque([(beginWord, 1)])

        parents = defaultdict(set)

        # depth_map dictionary holds how many steps it takes to reach a certain word
        # before appending a word to the queue you can check if he have already reached this word in less steps.
        # depth_map[word] holds a number indicating shortest amount of steps it takes to reach that word.
        depth_map = defaultdict(lambda: float("inf"))
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
                        parents[new_word].add(word)
                        depth_map[new_word] = steps + 1

            visited.add(word)

        answers = []

        def backtrack(path, word):
            if word == beginWord:
                answers.append(path)
                return

            for parent in parents[word]:
                backtrack([parent] + path, parent)

        backtrack([endWord], endWord)

        return answers


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
