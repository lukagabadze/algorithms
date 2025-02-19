"""

NOTE: I am getting time limit exceeded errors, I am NOT the GOAT today...
But I have an idea which might cut out some nodes I have to visit:
There are three reasons why we should check out the next node (append to the queue)
1) The path has not been visited yet `(node, next_node) not in visited_paths`
2) The node has not been visited yet `next_node not in visited_nodes`
3) The node has other unvisited nodes to offer us `len(set(graph[next_node]) - visited_nodes) > 0`

TODO: Fix this shit
"""

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph[0]:
            return 0

        # Number of nodes
        n = len(graph)

        answer = float("+inf")
        for i in range(len(graph)):
            queue = deque([(i, set(), set([i]))])
            found = False
            while queue:
                (node, visited_paths, visited_nodes) = queue.popleft()

                if found:
                    break

                for next_node in graph[node]:
                    if (node, next_node) not in visited_paths:
                        next_node_visited_paths = visited_paths.copy()
                        next_node_visited_paths.add((node, next_node))

                        next_node_visited_nodes = visited_nodes.copy()
                        next_node_visited_nodes.add(next_node)

                        if len(next_node_visited_nodes) == n:
                            answer = min(answer, len(next_node_visited_paths))
                            found = True

                        queue.append(
                            (
                                next_node,
                                next_node_visited_paths,
                                next_node_visited_nodes,
                            )
                        )

        return answer


if __name__ == "__main__":
    solution = Solution()

    # graph = [[1, 2, 3], [0], [0], [0]]

    # graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]

    graph = [
        [2, 10],
        [2, 7],
        [0, 1, 3, 4, 5, 8],
        [2],
        [2],
        [2],
        [8],
        [9, 11, 8, 1],
        [7, 6, 2],
        [7],
        [11, 0],
        [7, 10],
    ]

    # graph = [[2, 3], [7], [0, 6], [0, 4, 7], [3, 8], [7], [2], [5, 3, 1], [4]]

    for row in graph:
        print(" ".join(map(str, row)))
    print("\n")
    answer = solution.shortestPathLength(graph)
    print("answer: ", answer)
