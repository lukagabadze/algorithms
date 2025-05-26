"""
NOTE: I know this does NOT work. I just found out that Union Find does not work in directed graphs to detect cycles. 🥲
I will still commit this as a reminder.
"""

from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        colors = [ord(c) - ord("a") for c in colors]

        n = len(colors)
        parent = list(range(n))
        rank = [0] * n

        def find(node: int) -> int:
            if node != parent[node]:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int) -> bool:
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return False

            if rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
            elif rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1

            return True

        cm = [[0 for _ in range(26)] for _ in range(n)]
        answer = 0

        for a, b in edges:
            if not union(a, b):
                return -1

            for i in range(26):
                cm[b][i] = max(cm[b][i], cm[a][i])

            cm[b][colors[b]] += 1

            answer = max(answer, cm[b][colors[b]])

        return answer + 1


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]),
        ("a", [[0, 0]]),
        ("abacab", [[0, 1], [0, 2], [2, 3], [3, 4], [4, 1]]),
    ]

    for colors, edges in q:
        print("colors: ", colors)
        print("edges: ", edges)
        print()
        answer = solution.largestPathValue(colors, edges)
        print("answer: ", answer)
        print("=====================")
        print()
