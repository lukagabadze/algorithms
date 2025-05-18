from typing import List


"""
TIME: 28ms (Beats 5.82%)
NOTE: In this method I excluded an edge and unioned the rest of the edges, if it formed a tree, I returned True.
This method sucks and is super super slow.

TIME: 3ms (Beats 54.94%)
NOTE: This is much much much better.
Just union the edges until you detect a cycle.
Once a cycle forms, return the edge that caused it.
"""


class Solution(object):
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = list(range(n))
        rank = [0] * n

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return False

            if rank[a_root] >= rank[b_root]:
                parent[b_root] = a_root
            else:
                parent[a_root] = b_root

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]


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
