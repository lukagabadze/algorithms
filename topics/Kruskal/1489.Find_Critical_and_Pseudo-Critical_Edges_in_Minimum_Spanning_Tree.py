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

    def union(self, a: int, b: int) -> bool:
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return False

        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        elif self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = b_root
        else:
            self.parent[b_root] = a_root
            self.rank[a_root] += 1

        return True


"""
TIME: 815ms (Beats 16.35%)
MEMORY: 18.30MB (Beats 24.06%)
NOTE: This solution is super clean and it is almost 3x faster than my Prim solution.
But it is still very slow, I need to optimize it.

TIME: 805ms (Beats 17.23%)
NOTE: This is by just removing the print statement I left in there by accident.
It was only one line of print statement, it was not even in a loop so no significant improvements.

TIME: 445ms (Beats 82.77%)
NOTE: 2 improvements have been made that boosted the performance by 2x (thanks to ChatGPT!):
1) I added boolean return statements to the union method.
If it was successful it returs True, otherwise it returns False.
This makes it so I don't have to check if two nodes are connected with the find method before unioning them.

2) Instead of using find method inside the range(n) loop to check if all nodes were connected,
you can count all the unions you made, and if you made n - 1 unions (n - 1 edges), that means all n nodes have been connected.
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
        count = 0  # number of edges applied

        if include is not None:
            weight += edges[include][2]
            uf.union(edges[include][0], edges[include][1])
            count += 1

        for i, [s, e, w, _] in enumerate(edges):
            if i == block:
                continue

            # if the union was successful update the weight and the count
            if uf.union(s, e):
                weight += w
                count += 1

            # if n - 1 edges have been applied, that means we already unioned all n nodes
            if count == n - 1:
                break

        return weight if count == n - 1 else float("inf")


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
