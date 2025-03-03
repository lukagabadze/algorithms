from typing import List
from functools import cache


"""
TIME: 0ms (Beats 100%) GOAT! I AM THE GOAT!
"""


class Solution:
    wordSet = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = set(wordDict)
        return [" ".join(arr) for arr in self.dfs(s)]

    @cache
    def dfs(self, s: str) -> bool:
        sentences = []

        if s in self.wordSet:
            sentences.append([s])

        for i in range(1, len(s) + 1):
            if s[:i] in self.wordSet:
                for suffix in self.dfs(s[i:]):
                    sentences.append([s[:i]] + suffix)

        return sentences


if __name__ == "__main__":
    solution = Solution()

    # s = "catsanddog"
    # wordDict = ["cat", "cats", "and", "sand", "dog"]

    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]

    s = "aaaaaaa"
    wordDict = ["aaa", "aaaa", "a"]

    print("s: ", s)
    print("\n")
    answer = solution.wordBreak(s, wordDict)
    print("answer: ", answer)
