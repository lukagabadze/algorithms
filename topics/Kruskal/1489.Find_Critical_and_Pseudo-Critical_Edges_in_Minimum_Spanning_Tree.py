"""
NOTE: You need Union Find here to detect cycles because using Kruskal's algorithm means you will be selecting edges with the minimum weight,
and doing that means having selected edges that are scattered in the graph and you don't want to connect them as a cycle. IMO. This thought is still work in progress.
NOTE: Gabo 2 weeks later here, yes, you do need union find for that reason, to not connect already connected nodes using Krukal.

NOTE: MASSIVE thanks to Sunny Sharma for the most goated solution i have ever seen. It is explained super well with comments.
This is the only solution that actually made it click in my brain.
(https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/3929059/beats-100-js-ts-java-c-c-python-python3-kotlin)
"""

from typing import List, Optional


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]
        return node

    def union(self, a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return

        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        elif self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = b_root
        else:
            self.parent[b_root] = a_root
            self.rank[a_root] += 1


"""
TIME: 815ms (Beats 16.35%)
MEMORY: 18.30MB (Beats 24.06%)
NOTE: This solution is super clean and it is almost 3x faster than my Prim solution.
But it is still very slow, I need to optimize it.
"""


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        v = len(edges)
        critical, pseudo_critical = [], []

        # append the original index
        for i in range(v):
            edges[i].append(i)

        # sort based on index
        edges = sorted(edges, key=lambda x: x[2])

        mst_weight = self.mst(n, edges, None, None)

        print("mst_weight: ", mst_weight)

        for i in range(v):
            if mst_weight < self.mst(n, edges, i, None):
                critical.append(edges[i][3])
                continue

            if mst_weight == self.mst(n, edges, None, i):
                pseudo_critical.append(edges[i][3])
                continue

        return [critical, pseudo_critical]

    def mst(
        self,
        n: int,
        edges: List[List[int]],
        block: Optional[int],
        include: Optional[int],
    ) -> int:
        uf = UnionFind(n)
        weight = 0

        if include is not None:
            weight += edges[include][2]
            uf.union(edges[include][0], edges[include][1])

        for i, [s, e, w, _] in enumerate(edges):
            if i == block:
                continue

            if uf.find(s) == uf.find(e):
                continue

            uf.union(s, e)
            weight += w

        for i in range(n):
            if uf.find(0) != uf.find(i):
                return float("inf")

        return weight


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
        ),
        (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]),
        (
            6,
            [
                [0, 1, 1],
                [1, 2, 1],
                [0, 2, 1],
                [2, 3, 4],
                [3, 4, 2],
                [3, 5, 2],
                [4, 5, 2],
            ],
        ),
        (2, [[0, 1, 3]]),
        (3, [[0, 1, 1], [0, 2, 2], [1, 2, 3]]),
        (4, [[0, 1, 1], [0, 2, 2], [0, 3, 3]]),
    ]

    for n, edges in q:
        print("n: ", n)
        for row in edges:
            print(*row)
        print()
        answer = solution.findCriticalAndPseudoCriticalEdges(n, edges)
        print("answer: ", answer)
        print("=====================")
        print()
