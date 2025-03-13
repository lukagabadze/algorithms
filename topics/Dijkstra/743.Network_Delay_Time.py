"""
NOTE: Apparently the graph dict I am creating in the beginning is called an "adjacency list".

NOTE: I had a piece of code which looked like this: `answer = max(distance[i] for i in range(1, n + 1))`
This can be shortened like so: `answer = max(distance.values())`

TODO: It would be fun to write a heap queue on my own!
"""

from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency list
        graph = defaultdict(list)
        for s, e, time in times:
            graph[s].append((e, time))

        # It is important to have distance as the first element for the heap sort to work properly
        heap = [(0, k)]
        distance = {}

        while heap:
            (d, node) = heappop(heap)

            if node in distance:
                continue

            # This is the shortest path
            distance[node] = d

            for neighbour, time in graph[node]:
                # Push the node in the queue
                if neighbour not in distance:
                    heappush(heap, (d + time, neighbour))

        if len(distance) != n:
            return -1

        print("distance: ", distance)

        return max(distance.values())


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
            4,
            2,
        ),
        (
            [[1, 2, 1]],
            2,
            1,
        ),
        (
            [[1, 2, 1]],
            2,
            2,
        ),
        ([[1, 2, 1], [2, 1, 3]], 2, 2),
        ([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1),
    ]

    for times, n, k in q:
        print("times: ", times)
        print("n: ", n)
        print("k: ", k)
        answer = solution.networkDelayTime(times, n, k)
        print("answer: ", answer)
        print()
