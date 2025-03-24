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
        while heap:
            price, (time, node) = heappop(heap)

            if time > maxTime:
                continue

            if node == n:
                return price

            for neighbour, neighbour_time in graph[node]:
                new_time = time + neighbour_time
                new_price = price + passingFees[neighbour]
                if new_time <= maxTime and new_price < min_cost[neighbour]:
                    heappush(heap, (new_price, (new_time, neighbour)))
                    min_cost[neighbour] = new_price

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
