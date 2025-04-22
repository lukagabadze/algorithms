"""
NOTE: This code is slow, but it works and it gets accepted.
I came up with the solution:
The idea is that the possible root of a tree we are creating, should not have any parents.
So if we know that root, we can remove each edge one by one and run BFS from a the root (which we already found).
If the tree is a success without that edge, we return it.
(IMPORTANT: you must go through the edges backwards, since you want to return the last working extra edge in the input, hence the [::-1] in the possible edges array)

BUT, what if that the extra edge we are trying to find and remove was placed in a way that it covered up the root,
there are no nodes without a parent we can call the ROOT.
In that case, we take the nodes with the parent length of 1 and we know that the extra edge is attached to those nodes.
It is 100% one of those since otherwise we would have a root node wherever the tree starts.

NOTE: I will write a faster code probably with a fancy algorithm, but I am proud if this solution.
Took me about 30 minutes to come up with it and code it up!
"""

from typing import List
from collections import deque


"""
TIME: 304ms (Beats 5.20%)
MEMORY: 18.57MB (Beats 17.13%)
NOTE: This is because I am basically brute forcing with BFS 😁.
There is a better way to solve this with Union Find, but I have not learned it yet.
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        graph = [[] for _ in range(n)]
        parents = [[] for _ in range(n)]
        for a, b in edges:
            graph[a - 1].append(b - 1)
            parents[b - 1].append(a - 1)

        parent = parents.index([]) if [] in parents else None

        possible_edges = [[a - 1, b - 1] for a, b in edges]
        possible_parents = [parent]

        if parent is None:
            possible_edges = sorted(
                [
                    [parent, node]
                    for node, parents in enumerate(parents)
                    if len(parents) == 1
                    for parent in parents
                ],
                key=lambda x: edges.index([x[0] + 1, x[1] + 1]),
            )
            possible_parents = set(
                [
                    parent
                    for node, parents in enumerate(parents)
                    if len(parents) == 1
                    for parent in parents
                ]
            )

        for i, [a, b] in enumerate(possible_edges[::-1]):
            found = True

            for i in possible_parents:
                visited = set()
                queue = deque([(i, -1)])
                while queue:
                    node, parent = queue.popleft()

                    if node in visited:
                        found = False
                        break

                    visited.add(node)

                    for neighbour in graph[node]:
                        if node == a and neighbour == b:
                            continue

                        if neighbour not in visited:
                            queue.append((neighbour, node))

                if found and len(visited) == n:
                    return [a + 1, b + 1]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([[1, 2], [1, 3], [2, 3]]),
        ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]),
        ([[2, 1], [3, 1], [4, 2], [1, 4]]),
        ([[1, 2], [3, 1], [2, 3]]),
    ]

    for edges in q:
        for s, e in edges:
            print(s, e)
        print()
        answer = solution.findRedundantDirectedConnection(edges)
        print("answer: ", answer)
        print("=====================")
        print()
