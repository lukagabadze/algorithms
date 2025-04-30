"""
NOTE: It is at this point that I start to appreciate the problem giving me the number of nodes "n" as the parameter.
"""

from typing import List


"""
TIME: 43ms (Beats 57.28%)
NOTE: I AM FUCKING GOATED 😭
"""


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(node: int):
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return

            if rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
            elif rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1

        edges_available = 0
        for a, b in connections:
            a_root = find(a)
            b_root = find(b)

            # They are already connected
            if a_root == b_root:
                edges_available += 1
                continue

            union(a_root, b_root)

        roots = [find(i) for i in range(n)]

        # The nubmer of edges we need to change is equal
        # to the number of unique roots inside the roots array minus one.
        # This basically counts all the independent sections which need to be connected.
        # A section might be a set of nodes or just one node.
        # Either way, these sections need to connected
        changes_needed = len(set(roots)) - 1

        if edges_available < changes_needed:
            return -1
        else:
            return changes_needed


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1], [0, 2], [1, 2]]),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2]]),
    ]

    for n, connections in q:
        for row in connections:
            print(row)
        print()
        answer = solution.makeConnected(n, connections)
        print("answer: ", answer)
        print("=====================")
        print()
