"""
NOTE: I just realized something MASSIVE that I have been missing for last two months.
When you have a priority queue and you start running logic on neighbours and their weights,
you might put larger amount in your answers or min_distances array because that weight has not yet
reached the priority queue for it to be sorted.
That's why we check if this neighbour decreases my distance (or weight) before updating it.
And that's why we DON'T check if the node improves my distance when you run logic outside the
neighbour for loop, instead, when you run the code right after heappop and finding the node with the minimum weight (or distance).

NOTE: I finally solved this problem using Prim's Algorithm and you really do maintain a tree when you move through these points.
You start of from any point and just see all the nearest points. Then, if you connect you see all shortest points from there.
All these thanks to heapq for sorting my data.

NOTE: HUGE thanks to the GOAT niits on leetcode. (https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/6280134/video-improved-prim-s-algorithm-solution-python-javascript-java-and-c)
He also has a video on youtube which was the only tutorial that taught me something on this topic. (https://www.youtube.com/watch?v=zIHb5fCyjR8)
"""

from typing import List
from heapq import heappush, heappop


"""
TIME: 2430ms (Beats 28.79%)
MEMORY: 79.71MB (Beats 80.21%)
NOTE: This is just basic implementation of Prim's Algorithm without any caching improvements.

TIME: 390ms (Beats 97.16%)
MEMORY: 21.58 MB (Beats 91.85%)
NOTE: This is after adding the dist_cache array where I cache minimum distances that will arrive in the future,
I check new arrivals and if they are not lower than the cache, it's literally just useless to put it in the heapq,
because, the minimum distance I have in the dist_cache will one day rise up from the heapq and make its debut in the final dists array. (absolute cinema).

NOTE: One thing I was NOT expecting was for the memory to improve by this much!
But it makes sense, I introduced the dist_cache array and filled it with float('inf'),
BUT, I don't put useless garbage inside the heapq anymore, so it stays minimal,
thus, the 4x improvement on memory AND 6x improvement on time.

NOTE: This improvement also came from niits solution, so again, HUGE thanks to him!
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        dists = [0] * n
        visited = set()
        dist_cache = [float("inf")] * n
        while heap:
            distance, ind = heappop(heap)

            if ind in visited:
                continue

            dists[ind] = distance
            visited.add(ind)

            for point_ind in range(n):
                if point_ind in visited:
                    continue

                point_distance = abs(points[ind][0] - points[point_ind][0]) + abs(
                    points[ind][1] - points[point_ind][1]
                )

                if point_distance < dist_cache[point_ind]:
                    dist_cache[point_ind] = point_distance
                    heappush(heap, (point_distance, point_ind))

        return sum(dists)


if __name__ == "__main__":
    solution = Solution()

    q = [
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]],
        [[2, -3], [-17, -8], [13, 8], [-17, -15]],
    ]

    for points in q:
        print("points: ", *points)
        print()
        answer = solution.minCostConnectPoints(points)
        print("answer: ", answer)
        print("=====================")
        print()
