"""
NOTE: While assembling the graph I had the code looking like this:

        graph = defaultdict(list)
        for i, (node1, node2) in enumerate(edges):
            graph[node1].append((node2, -succProb[i]))

This code is incorrect because the problem states that the graph is UNDIRECTED.
What I am assembling here is a DIRECTED graph.
The code should look like this when you are dealing with an undirected graph:

        graph = defaultdict(list)
        for i, (node1, node2) in enumerate(edges):
            graph[node1].append((node2, -succProb[i]))
            graph[node2].append((node1, -succProb[i]))
"""

from typing import List
from collections import defaultdict
from heapq import heappop, heappush


"""
TIME: 215ms (Beats 9.81%)

NOTE: Maybe this problem does NOT require Dijkstra's algorithm.
Why is it this slow?

NOTE: Looks like this problem is supposed to be solved
with Bellman Ford's algorithm for maximum performance.
"""


"""
TIME: 215ms (Beats 9.07%)
MEMORY: 30.56MB (Beats 6.68%)
NOTE: This is with graph and probs as dictionaries.

TIME: 185ms (Beats 11.56%)
MEMORY: 29.25MB (Beats 38.04%)
NOTE: This is by just switching graph and probs from dictionaries to arrays.
"""


class Solution(object):
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph = [[] for _ in range(n)]
        for i, (node1, node2) in enumerate(edges):
            graph[node1].append((node2, succProb[i]))
            graph[node2].append((node1, succProb[i]))

        heap = [(-1, start_node)]
        probs = [0] * n
        while heap:
            (prob, node) = heappop(heap)

            if probs[node] != 0:
                continue

            probs[node] = prob

            for neighbour, n_prob in graph[node]:
                heappush(heap, (prob * n_prob, neighbour))

        return probs[end_node] * -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),
        (
            5,
            [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
            [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
            3,
            4,
        ),
        (3, [[0, 1]], [0.5], 0, 2),
    ]

    for n, edges, succProb, start, end in q:
        print("n: ", n)
        print("edges: ", edges)
        print("succProb: ", succProb)
        print("start: ", start)
        print("end: ", end)
        answer = solution.maxProbability(n, edges, succProb, start, end)
        print("answer: ", answer)
        print()
