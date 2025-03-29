"""
NOTE: This problem is a very good mix of DP + Binary Search.
It is beautfiul.
"""

from typing import List


class Solution(object):
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        return 0


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]),
        ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]),
        ([1, 1, 1], [2, 3, 4], [5, 6, 4]),
        (
            [6, 15, 7, 11, 1, 3, 16, 2],
            [19, 18, 19, 16, 10, 8, 19, 8],
            [2, 9, 1, 19, 5, 7, 3, 19],
        ),
        (
            [24, 24, 7, 2, 1, 13, 6, 14, 18, 24],
            [27, 27, 20, 7, 14, 22, 20, 24, 19, 27],
            [6, 1, 4, 2, 3, 6, 5, 6, 9, 8],
        ),
    ]

    for startTime, endTime, profit in q:
        for i in range(len(startTime)):
            print(f"{i}: {(startTime[i], endTime[i], profit[i])}")
        print()
        answer = solution.jobScheduling(startTime, endTime, profit)
        print("answer: ", answer)
        print("=====================")
        print()
