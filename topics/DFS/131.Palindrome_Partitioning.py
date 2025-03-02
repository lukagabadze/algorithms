"""
NOTE: You put len(s) + 1 inside the range end parameter so you can check the entire string.
If you don't put that + 1, the entire string might be a palindrome and you might miss it.

NOTE: I could not solve this on my own, HUGE thanks to the GOAT Lynn!
(https://leetcode.com/problems/palindrome-partitioning/solutions/1667786/python-simple-recursion-detailed-explanation-easy-to-understand)

NOTE: It's my first time using @cache from functools, I did not even know it had to be imported.
It's really interesting and speeds up the algorithm 6 times!!!
Basically, once you compute all partitions for a substring 'aab' for example, you can cache it and
next time you see 'aab' you can just return the array of possibilities you already computed once!
"""

from functools import cache


class Solution:
    @cache
    def partition(self, s: str):
        # Base Cases
        if not s:
            return [[]]

        ans = []

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for suffix in self.partition(s[i:]):
                    ans.append([s[:i]] + suffix)

        return ans


if __name__ == "__main__":
    solution = Solution()

    # s = "aaabbaca"

    # s = "aab"

    # s = "a"

    s = "aa"

    print("s: ", s)
    print("\n")
    answer = solution.partition(s)
    print("answer: ", answer)
