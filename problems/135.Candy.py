"""
NOTE: Thanks to Arun Kumar for the clean solution!
(https://leetcode.com/problems/candy/solutions/6803186/easy-to-understand-approach)
"""

from typing import List


class Solution(object):
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Left-to-Right
        l2r = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                l2r[i] = l2r[i - 1] + 1

        r2l = [1] * n
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                r2l[i] = r2l[i + 1] + 1

        answer = 0
        for i in range(n):
            answer += max(l2r[i], r2l[i])

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 0, 2]),
        ([1, 2, 2]),
        ([7, 6, 9, 3, 4, 6, 10]),
        ([0, 1, 2, 3, 2, 1]),
        ([1, 2, 87, 87, 87, 2, 1]),
    ]

    for ratings in q:
        print("ratings: ", ratings)
        print()
        answer = solution.candy(ratings)
        print("answer: ", answer)
        print("=====================")
        print()
