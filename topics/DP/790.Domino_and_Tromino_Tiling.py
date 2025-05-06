"""
NOTE: Thanks to Sparsh Choudhary for the solution! (https://leetcode.com/problems/domino-and-tromino-tiling/solutions/6716200/beats-super-easy-beginners-java-c-c-python-javascript-dart)

NOTE: Also very goated explanation image can be found here:
https://leetcode.com/problems/domino-and-tromino-tiling/description/comments/1566271/
"""


class Solution(object):
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 2, 5]

        for i in range(3, n):
            dp.append((2 * dp[i - 1] + dp[i - 3]) % MOD)

        return dp[n - 1]


if __name__ == "__main__":
    solution = Solution()

    q = [(1), (2), (3), (4), (5), (6), (8)]

    for n in q:
        print("n: ", n)
        print()
        answer = solution.numTilings(n)
        print("answer: ", answer)
        print("=====================")
        print()
