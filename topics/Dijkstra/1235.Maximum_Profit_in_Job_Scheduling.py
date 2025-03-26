from typing import List
from collections import defaultdict
from heapq import heappop, heappush


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
    ]

    for startTime, endTime, profit in q:
        for i in range(len(startTime)):
            print((startTime[i], endTime[i], profit[i]))
        print()
        answer = solution.jobScheduling(startTime, endTime, profit)
        print("answer: ", answer)
        print("=====================")
        print()
