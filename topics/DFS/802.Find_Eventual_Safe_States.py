from collections import defaultdict
from typing import List


"""
TIME: 59ms (Beats 33.18%)
Complexity: O(n)
This is my own solution, let's think how this can be improved, might take a look in solutions tab.
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        answers_map = defaultdict(lambda: None)
        visited = set()

        def dfs(node: int):
            if answers_map[node] is not None:
                return answers_map[node]

            neighbours = []
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    neighbours.append(dfs(next_node))
                else:
                    neighbours.append(answers_map[next_node])

            is_safe = all(neighbours)
            answers_map[node] = is_safe
            return is_safe

        for i in range(n):
            dfs(i)

        return [i for i in range(n) if answers_map[i] is True]


if __name__ == "__main__":
    solution = Solution()

    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    # graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]

    for i, row in enumerate(graph):
        print(i, end=": ")
        print(" ".join(map(str, row)))
    print("\n")
    answer = solution.eventualSafeNodes(graph)
    print("answer: ", answer)
