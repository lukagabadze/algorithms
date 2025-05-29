from typing import List
from collections import deque


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

        def find_even_count(graph: List[List[int]], start: int) -> int:
            queue = deque([(start, 0, -1)])
            count = 0
            while queue:
                node, depth, parent = queue.popleft()

                if depth % 2 == 0:
                    count += 1

                for neighbour in graph[node]:
                    if neighbour != parent:
                        queue.append((neighbour, depth + 1, node))

            return count

        # Find the max even count of the second tree.
        # It is either the count from the root or count from one of the roots children.
        second_tree_max_even_count = max(
            find_even_count(graph2, 0), find_even_count(graph2, graph2[0][0])
        )

        # Map out every node from the first tree as odds and evens.
        node_even = [False] * n
        queue = deque([(0, 0, -1)])
        while queue:
            node, depth, parent = queue.popleft()

            if depth % 2 == 0:
                node_even[node] = True

            for neighbour in graph1[node]:
                if neighbour != parent:
                    queue.append((neighbour, depth + 1, node))

        # If a node is even we should add the odd count to the answer,
        # otherwise, if its depth is odd, add even count.
        odd_count = find_even_count(graph1, 0)
        even_count = find_even_count(graph1, graph1[0][0])
        answers = []
        for i in range(n):
            count = second_tree_max_even_count

            if node_even[i]:
                count += odd_count
            else:
                count += even_count

            answers.append(count)

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
