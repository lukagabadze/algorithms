from typing import List
from collections import deque


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Base Case
        if k == 0:
            return [1] * n

        graph1 = [[] for _ in range(n)]
        for s, e in edges1:
            graph1[s].append(e)
            graph1[e].append(s)

        graph2 = [[] for _ in range(m)]
        for s, e in edges2:
            graph2[s].append(e)
            graph2[e].append(s)

        def find_count(graph: List[List[int]], start: int, limit: int) -> int:
            queue = deque([(start, 0)])
            visited = set([start])
            count = 1
            while queue:
                node, depth = queue.popleft()

                if depth >= limit:
                    break

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, depth + 1))
                        visited.add(neighbour)
                        count += 1

            return count

        second_tree_max_count = 0
        for j in range(m):
            count = find_count(graph2, j, k - 1)
            second_tree_max_count = max(second_tree_max_count, count)

        answers = []
        for i in range(n):
            count = find_count(graph1, i, k)
            answers.append(second_tree_max_count + count)

        return answers


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            [[0, 1], [0, 2], [2, 3], [2, 4]],
            [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
            2,
        ),
        ([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]], 1),
        ([[0, 1]], [[0, 1]], 0),
        ([[0, 1]], [[0, 1]], 1),
    ]

    for edges1, edges2, k in q:
        print("edges1: ", edges1)
        print("edges2: ", edges2)
        print("k: ", k)
        print()
        answer = solution.maxTargetNodes(edges1, edges2, k)
        print("answer: ", answer)
        print("=====================")
        print()
