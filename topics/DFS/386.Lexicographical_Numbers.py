"""
NOTE: Thanks to Priyanshu Pandey for the easy solution!
(https://leetcode.com/problems/lexicographical-numbers/solutions/6821610/100-beat-o-n-log-n-o-n-o-1-space-from-sorting-to-dfs-lexico-mastery)
"""

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answers = []

        def dfs(s: int):
            if s > n:
                return

            answers.append(s)

            for i in range(0, 10):
                next_num = s * 10 + i
                if next_num > n:
                    return

                dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return answers


if __name__ == "__main__":
    solution = Solution()

    q = [(13), (2), (2000)]

    for n in q:
        print("n: ", n)
        print()
        answer = solution.lexicalOrder(n)
        print("answer: ", answer)
        print("=====================")
        print()
