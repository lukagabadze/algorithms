"""
NOTE: Huge thanks to KameshKadimisetty for the solution!
(https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/6491759/simple-dijkstra-s-algorithm-c)

NOTE: This solution is a bit different than the normal Dijkstra.
It goes to a certain node only if the price gets decreased.
And also, it uses the distance to sort the min_heap, not price which is very very interesting.
This way, we might see some nodes repeated in the heap, which is not something I saw in previous Dijsktra problems.

TODO: I don't quite understand the details of this solution yet, I need to
look into it more and completely write the explanation here!
"""

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

        heap = [(0, (0, src))]
        prices = defaultdict(lambda: float("inf"))
        while heap:
            (distance, (price, node)) = heappop(heap)

            if distance > k:
                break

            for neighbour, n_price in graph[node]:
                # If going to the neighbour decreases my price,
                # update the prices dict and push the node to the heap.
                if price + n_price < prices[neighbour]:
                    prices[neighbour] = price + n_price
                    heappush(heap, (distance + 1, (price + n_price, neighbour)))

        if dst in prices:
            return prices[dst]

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
        (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1),
        (4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 2),
    ]

    for n, flights, src, dst, k in q:
        print("n: ", n)
        print("flights: ", flights)
        print("src: ", src)
        print("dst: ", dst)
        print("k: ", k)
        print()
        answer = solution.findCheapestPrice(n, flights, src, dst, k)
        print("answer: ", answer)
        print("=====================")
        print()
