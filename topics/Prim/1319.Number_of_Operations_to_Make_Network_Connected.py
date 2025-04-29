from typing import List
from collections import deque


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)

        queue = deque([connections[0][0]])
        weight = -1
        visited = set()
        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            weight += 1
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

        nodes_left_to_visit = (n - 1) - weight
        edges_left = len(connections) - weight

        if edges_left >= nodes_left_to_visit:
            return nodes_left_to_visit

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1], [0, 2], [1, 2]]),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]),
        (6, [[0, 1], [0, 2], [0, 3], [1, 2]]),
    ]

    for n, connections in q:
        print("n: ", n)
        for row in connections:
            print(row)
        print()
        answer = solution.makeConnected(n, connections)
        print("answer: ", answer)
        print("=====================")
        print()
