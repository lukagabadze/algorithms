from collections import deque, defaultdict
from typing import List


"""
TIME: 3ms (Beats 93.52%)
NOTE: This problem is very similar to word ladder II which was a huge pain in the ass.
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source = 0
        target = n - 1

        stack = deque([source])
        visited = set()
        parents = defaultdict(list)

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            for next_node in graph[node]:
                stack.append(next_node)
                parents[next_node].append(node)

            visited.add(node)

        answers = []

        def backtrack(path, node):
            if node == source:
                answers.append(path)
            else:
                for parent in parents[node]:
                    backtrack([parent] + path, parent)

        backtrack([target], target)
        return answers


if __name__ == "__main__":
    solution = Solution()

    # graph = [[1, 2], [3], [3], []]

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    for i, row in enumerate(graph):
        print(i, end=": ")
        print(" ".join(map(str, row)))
    print("\n")
    answer = solution.allPathsSourceTarget(graph)
    print("answer: ", answer)
