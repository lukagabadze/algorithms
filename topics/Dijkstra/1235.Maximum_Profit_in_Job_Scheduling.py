"""
NOTE: ChatGPT Told me this was a hard problem to practice Dijkstras algorithm.
Well that was a fucking lie.

This problem is solved using DP + Binary Search.
It's really really awesome so I will be moving it to the DP folder.

I will still keep this implementation because it works (if you don't consider the fact it gets TLE 🤭).
"""

from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)

        # Assemble the paths tuple array so I can sort it
        paths = []
        for i in range(len(startTime)):
            paths.append((startTime[i], endTime[i], profit[i]))
        paths = sorted(paths)

        # Each item of the heap contains (money, time_index)
        heap = []
        answers = defaultdict(int)

        i = 0
        while i < n and paths[0][1] > paths[i][0]:
            heappush(heap, (-paths[i][2], i))
            i += 1

        while heap:
            money, time_ind = heappop(heap)

            answers[time_ind] = min(money, answers[time_ind])

            i = time_ind + 1

            # Move the index to the nearest neighbour
            while i < n and paths[i][0] < paths[time_ind][1]:
                i += 1

            # Go through all the neighbours.
            # Neighbours are all sequential paths until we meet one path where
            # its startTime is more than max endTime we saw in the neighbours.
            max_end = float("inf")
            while i == n - 1 or (i < n and max_end > paths[i + 1][0]):
                heappush(heap, (money - paths[i][2], i))

                if i != n - 1:
                    max_end = max(max_end, paths[i + 1][1])

                i += 1

        return -min(answers.values())


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
