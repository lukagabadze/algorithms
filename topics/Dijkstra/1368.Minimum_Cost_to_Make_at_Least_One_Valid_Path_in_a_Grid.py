"""
NOTE: DAAAAMNN I Solved this in 12 fucking minutes! I am becoming the fucking GOAT!

NOTE: I can't believe I got this far in two months, practicing every day really does add up over time.
Two months ago, I would not even try solving this problem since the label on leetcode said 'HARD'.
One month ago, I would try it and waste hours on it and then check the solutions tab.
But now, I can just code this simple Dijkstra solution in 12 minutes and submit it successfuly on the first try! 🐐🐐🐐
"""

from typing import List
from heapq import heappop, heappush


class Solution(object):
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        heap = [(0, (0, 0))]
        costs = [[float("inf") for _ in range(n)] for _ in range(m)]
        while heap:
            cost, (i, j) = heappop(heap)

            if i == m - 1 and j == n - 1:
                return cost

            for key in directions:
                di, dj = directions[key]
                x, y = i + di, j + dj

                if x >= 0 and y >= 0 and x < m and y < n:
                    new_cost = cost + 1 if key != grid[i][j] else cost

                    if new_cost < costs[x][y]:
                        heappush(heap, (new_cost, (x, y)))
                        costs[x][y] = new_cost


if __name__ == "__main__":
    solution = Solution()

    q = [
        [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]],
        [[1, 1, 3], [3, 2, 2], [1, 1, 4]],
        [[1, 2], [4, 3]],
    ]

    for heights in q:
        for row in heights:
            print(row)
        print()
        answer = solution.minCost(heights)
        print("answer: ", answer)
        print("=====================")
        print()
