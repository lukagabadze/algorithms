from typing import List


"""
TIME: 28ms (Beats 5.82%)
NOTE: In this method I excluded an edge and unioned the rest of the edges, if it formed a tree, I returned True.
This method sucks and is super super slow.
"""


class Solution(object):
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return

            if rank[a_root] >= rank[b_root]:
                parent[b_root] = a_root
            else:
                parent[a_root] = b_root

        # Exclude egdes in reversed since they ask for the answer that occurs last in the input.
        for excluded_node_index in reversed(range(n)):
            parent = list(range(n))
            rank = [0] * n

            for i, [a, b] in enumerate(edges):
                if i == excluded_node_index:
                    continue

                # The node numbers in the input start from 1 instead of 0
                # so I have to subtract 1 from them so they can fit in the array
                union(a - 1, b - 1)

            roots = [find(i) for i in parent]
            if all(x == roots[1] for x in roots):
                return edges[excluded_node_index]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([[1, 2], [1, 3], [2, 3]]),
        ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]),
        (
            [
                [9, 10],
                [5, 8],
                [2, 6],
                [1, 5],
                [3, 8],
                [4, 9],
                [8, 10],
                [4, 10],
                [6, 8],
                [7, 9],
            ]
        ),
        (
            [
                [2, 7],
                [7, 8],
                [3, 6],
                [2, 5],
                [6, 8],
                [4, 8],
                [2, 8],
                [1, 8],
                [7, 10],
                [3, 9],
            ]
        ),
    ]

    for edges in q:
        for s, e in edges:
            print(s, e)
        print()
        answer = solution.findRedundantConnection(edges)
        print("answer: ", answer)
        print("=====================")
        print()
