"""
NOTE: While solving this problem using Disjtoint Set Union without using the "Union By Rank" optimization you WILL get TLE.
(https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/)

NOTE: I noticed in small testcases that parent array and [find(i) for i in parent] were always the same.
So I tried the following inside the union function, instead of having this code:
        root_x = find(x)
        root_y = find(y)

I placed:
        root_x = parent[x]
        root_y = parent[y]

Which resulted in the parent array getting messed up and an infinite cycle inside the find function 😁.
"""

from typing import List


"""
TIME: 232ms (Beats 97.71%)
MEMORY: 83.34MB (Beats 96.08%)
NOTE: Using Disjoint Set Union with Union By Rank optimization gives O(E*log(E)) time which is suprisingly faster than other solutions like BFS and DFS.

TIME: 199ms (Beats 98.82%)
MEMORY: 83.40MB (Beats 96.07%)
NOTE: I just added a simple check inside the union function which checks if root_x == root_y then they are already in the same group, no need to "union" them.
"""


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        parent = list(range(n))
        rank = [0] * n

        def find(n: int):
            while parent[n] != n:
                n = parent[n]
            return n

        def union(x: int, y: int):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = parent[root_x]
                rank[root_x] += 1

        for x, y in edges:
            union(x, y)

        return find(source) == find(destination)


if __name__ == "__main__":
    solution = Solution()

    q = [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5),
    ]

    for n, edges, source, destination in q:
        print("n: ", n)
        for row in edges:
            print(*row)
        print("source: ", source)
        print("destination: ", destination)
        print()
        answer = solution.validPath(n, edges, source, destination)
        print("answer: ", answer)
        print("=====================")
        print()
