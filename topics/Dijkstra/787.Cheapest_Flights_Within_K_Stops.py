from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        for node1, node2, price in flights:
            graph[node1].append((node2, price))

        heap = [(0, 0, src)]
        prices = {}
        while heap:
            (price, distance, node) = heappop(heap)

            if node in prices:
                continue

            prices[node] = price

            if distance > k:
                continue

            for neighbour, n_price in graph[node]:
                heappush(heap, (price + n_price, distance + 1, neighbour))

        if dst in prices:
            return prices[dst]

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        # (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
        # (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
        # (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1),
        # (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 2),
    ]

    for n, flights, src, dst, k in q:
        print("n: ", n)
        print("flights: ", flights)
        print("src: ", src)
        print("dst: ", dst)
        print("k: ", k)
        answer = solution.findCheapestPrice(n, flights, src, dst, k)
        print("answer: ", answer)
        print()
