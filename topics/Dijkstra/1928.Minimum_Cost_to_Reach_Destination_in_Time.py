"""
NOTE: After days of getting MLE, TLE, Wrong Answer on this problem, I finally solved it!
I just added min_time dictionary next to the min_cost dictionary.
And I go to a node only if one of these metrics can be improved by going there, either time or the price.
Before, I only went to a node if it improved my pricing and did not go over the maxTime limit.
But now, I can take any fucking improvements because my solution was NOT getting accepted.
"""

from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def minCost(
        self, maxTime: int, edges: List[List[int]], passingFees: List[int]
    ) -> int:
        graph = defaultdict(list)
        n = 0
        for node1, node2, time in edges:
            graph[node1].append((node2, time))
            graph[node2].append((node1, time))
            n = max(n, node1, node2)

        # Each item of the heap contains (price, (time, node))
        heap = [(passingFees[0], (0, 0))]
        min_cost = defaultdict(lambda: float("inf"))
        min_time = defaultdict(lambda: float("inf"))
        while heap:
            price, (time, node) = heappop(heap)

            if node == n:
                return price

            for neighbour, neighbour_time in graph[node]:
                new_time = time + neighbour_time
                new_price = price + passingFees[neighbour]

                if new_time > maxTime:
                    continue

                # If time or price can be improved
                # put the neighbour in the queue
                if new_time < min_time[neighbour] or new_price < min_cost[neighbour]:
                    heappush(heap, (new_price, (new_time, neighbour)))
                    min_cost[neighbour] = min(new_price, min_cost[neighbour])
                    min_time[neighbour] = min(new_time, min_time[neighbour])

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            30,
            [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
            [5, 1, 2, 20, 20, 3],
        ),
        (
            29,
            [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
            [5, 1, 2, 20, 20, 3],
        ),
        (
            25,
            [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]],
            [5, 1, 2, 20, 20, 3],
        ),
    ]

    for maxTime, edges, passingFees in q:
        print("maxTime: ", maxTime)
        for node1, node2, time in edges:
            print(f"{node1} -> {node2}  time={time}")
        for i, row in enumerate(passingFees):
            print(f"{i}: {row}")
        print()
        answer = solution.minCost(maxTime, edges, passingFees)
        print("answer: ", answer)
        print("=====================")
        print()
