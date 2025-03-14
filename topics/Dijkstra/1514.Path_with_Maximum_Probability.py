from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        return 0


if __name__ == "__main__":
    solution = Solution()

    q = [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),
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
