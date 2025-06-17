"""
NOTE: Huge thanks to An-Wen Deng for the solution!
(https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/solutions/6852136/combinatorics-number-theory-optimized-to-0ms)

I need to practice Combinatorics more!
"""

from math import comb


class Solution(object):
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        return (comb(n - 1, k) % MOD) * m * pow(m - 1, n - 1 - k, mod=MOD) % MOD


if __name__ == "__main__":
    solution = Solution()

    q = [
        (3, 2, 1),
        (4, 2, 2),
        (5, 2, 0),
    ]

    for n, m, k in q:
        print("n: ", n)
        print("m: ", m)
        print("k: ", k)
        print()
        answer = solution.countGoodArrays(n, m, k)
        print("answer: ", answer)
        print("=====================")
        print()
