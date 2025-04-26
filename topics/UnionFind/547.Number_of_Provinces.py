from typing import List


"""
TIME: 8ms (Beats 38.05%)
MEMORY: 19.14MB (Beats 42.20%)
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        parent = list(range(n))
        rank = [0] * n

        def find(node: int):
            while parent[node] != node:
                node = parent[node]
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

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    union(i, j)

        return len(set([find(i) for i in parent]))


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]]),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ]

    for isConnected in q:
        for row in isConnected:
            print(row)
        print()
        answer = solution.findCircleNum(isConnected)
        print("answer: ", answer)
        print("=====================")
        print()
