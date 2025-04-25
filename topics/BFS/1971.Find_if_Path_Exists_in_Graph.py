from typing import List
from collections import deque


"""
TIME: 293ms (Beats 92.28%)
MEMORY: 85.25MB (Beats 89.84%)
"""


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = set()
        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if neighbour == destination:
                        return True

                    queue.append(neighbour)
                    visited.add(neighbour)

        return False


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
