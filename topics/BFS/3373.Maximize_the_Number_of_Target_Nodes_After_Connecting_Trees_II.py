from typing import List
from collections import deque


"""
TIME: 713ms (Beats 19.32%)
NOTE: Initial result.

TIME: 483ms (Beats 62.50%)
NOTE: I was counting even nodes from the root and from the child of the root in two different BFS calls.
You can merge them in one, since EVEN nodes count from the "child of the root" is ODD nodes count from the "root".
I also fill the answers array in the last BFS where I check for even and odd depths of the first tree.
"""


class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = [[] for _ in range(n)]
        for s, e in edges1:
            graph1[s].append(e)
            graph1[e].append(s)

        graph2 = [[] for _ in range(m)]
        for s, e in edges2:
            graph2[s].append(e)
            graph2[e].append(s)

        def find_odd_and_even_counts(graph: List[List[int]]) -> int:
            queue = deque([(0, 0, -1)])
            even = 0
            odd = 0
            while queue:
                node, depth, parent = queue.popleft()

                if depth % 2 == 0:
                    even += 1
                else:
                    odd += 1

                for neighbour in graph[node]:
                    if neighbour != parent:
                        queue.append((neighbour, depth + 1, node))

            return [odd, even]

        # Find the max count of the second tree between odd and even depths.
        second_tree_max_even_count = max(find_odd_and_even_counts(graph2))

        even_count, odd_count = find_odd_and_even_counts(graph1)
        answers = [second_tree_max_even_count] * n
        queue = deque([(0, 0, -1)])
        while queue:
            node, depth, parent = queue.popleft()

            if depth % 2 == 0:
                answers[node] += odd_count
            else:
                answers[node] += even_count

            for neighbour in graph1[node]:
                if neighbour != parent:
                    queue.append((neighbour, depth + 1, node))

        return answers


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            [[0, 1], [0, 2], [2, 3], [2, 4]],
            [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
        ),
        ([[0, 1], [0, 2], [0, 3], [0, 4]], [[0, 1], [1, 2], [2, 3]]),
        ([[0, 1]], [[0, 1]]),
    ]

    for edges1, edges2 in q:
        print("edges1: ", edges1)
        print("edges2: ", edges2)
        print()
        answer = solution.maxTargetNodes(edges1, edges2)
        print("answer: ", answer)
        print("=====================")
        print()
