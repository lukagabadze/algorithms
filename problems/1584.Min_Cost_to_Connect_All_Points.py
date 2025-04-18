"""
NOTE: This code was written by me inside the subway using my phone...
my fucking phone.

I did not have time today to practice on my computer so I had to pull out my phone inside the subway.
It was painful, and my code did NOT do well. But I'm still proud.

It's currently 1:48 AM so I will commit this with the time of 20:39.
That's when I submitted my code, so we will call this attempt number 1.
"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        answer = 0
        for i, [x1, y1] in enumerate(points):
            if i in visited:
                continue

            min_point = -1
            min_dist = float("inf")
            for j, [x2, y2] in enumerate(points):
                dist = abs(x2 - x1) + abs(y2 - y1)
                if i != j and j not in visited and dist < min_dist:
                    min_point = j
                    min_dist = dist

            if min_point != -1:
                answer += min_dist
                visited.add(i)
                visited.add(min_point)

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]],
    ]

    for points in q:
        print("points: ", *points)
        print()
        answer = solution.minCostConnectPoints(points)
        print("answer: ", answer)
        print("=====================")
        print()
