"""
NOTE: My Dijkstra solutions are passing but they are performing worse than the average.
I don't know why that is, maybe these problems are better suited for Bellman Ford algorithm or something, idk I have not learned it yet.

NOTE: Cool python syntax:
        m = len(heights)
        n = len(heights[0])

This can be changed into:
        m, n = len(heights), len(heights[0])

And this:
        x = i + dx
        y = j + dy

into:
        x, y = i + dx, j + dy
"""

from typing import List
from heapq import heappop, heappush


"""
TIME: 734ms (Beats 22.76%)
NOTE: Can be improved!

TIME: 554ms (Beats 28.61%)
NOTE: Exitting early while finding the answer for the target seems to speed things up, but not quite enough.

TIME: 401ms (Beats 43.66%)
MEMORY: 19.73MB (Beats 50.66%)
NOTE: I moved the efforts logic into the directions loop and it seems to have speed up the solution, BUT HOW THO???
This was kinda the case in 1514 as well, where moving the logic inside the directions loop solved my problems.
NOTE: Gabo one month later here, I was pusing all the points_of_interest without checking if it improved my efforts dictionary.
That's why putting the logic outside the for loop worked slower. It basically had no caching, it would push everything into the heapq until every cell was covered. (I think).

TIME: 305ms (Beats 70.87%)
MEMORY: 19.16MB (Beats 90.47%)
NOTE: I just replaced the efforts dictionary into an efforts matrix.
Generally arrays are faster than dictionaries. Hence the great result!

TIME: 286ms (Beats 79.38%)
MEMORY: 19.65MB (Beats 54.16%)
NOTE: I just prebinded value of infinity:
    INF = float('inf')
And suprisingly it improved my time a little bit. Thanks to ChatGPT for the idea.

I also tried changing the if statement where I check if x and y are in bounds from:
    if x >= 0 and y >= 0 and x < m and y < n:
to:
    if 0 <= x < m and 0 <= y < n:
But it did not make any performance difference in this case.

I ALSO tried adding `efforts[0][0] = 0` but it did not impact performance.
"""


class Solution(object):
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = float("inf")
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Heap containing (effort, (row, col))
        heap = [(0, (0, 0))]
        efforts = [[INF for _ in range(n)] for _ in range(m)]
        efforts[0][0] = 0
        while heap:
            (effort, (i, j)) = heappop(heap)

            if i == m - 1 and j == n - 1:
                return effort

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    new_effort = max(
                        effort,
                        abs(heights[x][y] - heights[i][j]),
                    )

                    if new_effort < efforts[x][y]:
                        efforts[x][y] = new_effort
                        heappush(heap, (new_effort, (x, y)))


if __name__ == "__main__":
    solution = Solution()

    q = [
        [[1, 2, 2], [3, 8, 2], [5, 3, 5]],
        [[1, 2, 3], [3, 8, 4], [5, 3, 5]],
        [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ],
        [[1, 10, 6, 7, 9, 10, 4, 9]],
    ]

    for heights in q:
        for row in heights:
            print(row)
        print()
        answer = solution.minimumEffortPath(heights)
        print("answer: ", answer)
        print("=====================")
        print()
