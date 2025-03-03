from typing import List
from functools import cache


"""
TIME: 3ms (Beats 68.93%)

NOTE: Very similar to palindrome partitioning!
You just check every prefix and run recursion on the suffix. Pretty cool!
"""


class Solution:
    wordSet = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordSet = set(wordDict)
        return self.dfs(s)

    @cache
    def dfs(self, s: str) -> bool:
        if s in self.wordSet:
            return True

        for i in range(1, len(s) + 1):
            if s[:i] in self.wordSet:
                if self.dfs(s[i:]):
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()

    # s = "leetcode"
    # wordDict = ["leet", "code"]

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    print("s: ", s)
    print("\n")
    answer = solution.wordBreak(s, wordDict)
    print("answer: ", answer)
