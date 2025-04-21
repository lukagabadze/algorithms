"""
NOTE: "1 <= ai < bi <= edges.length" This constraint might be the KEY to returning the last edge in the input in case of multiple answers.
Because currently I have NO clue how I can find the last edge in the input in O(n) time.
"""

from typing import List
from collections import deque


"""
TIME: 11ms (Beats 15.07%)
MEMORY: 18.14MB (Beats 78.34%)
NOTE: I don't like this, I need to improve this.

TIME: 8ms (Beats 16.68%)
MEMORY: 18.25MB (Beats 57.76%)
NOTE: Not using a heap (priority queue) and just using deque saved me 3ms. But it is still NOT enough.
"""


class Solution(object):
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i, [a, b] in enumerate(edges[::-1]):
            queue = deque([(1, -1)])
            visited = set()
            found = True
            while queue:
                node, parent = queue.popleft()

                if node in visited:
                    found = False
                    break

                visited.add(node)

                for neighbour in graph[node]:
                    if min(node, neighbour) == a and max(node, neighbour) == b:
                        continue

                    if neighbour not in visited:
                        queue.append((neighbour, node))

            if found and len(visited) == n:
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
