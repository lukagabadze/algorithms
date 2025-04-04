from typing import List
from collections import defaultdict


class Solution(object):
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            a = "".join(sorted(a))
            b = "".join(sorted(b))
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        answers = []
        for source, target in queries:
            source = "".join(sorted(source))
            target = "".join(sorted(target))

            queue = [(source, 1)]
            visited = set()
            answer = -1

            while queue:
                node, value = queue.pop(0)

                for neighbour, neighbour_value in graph[node]:
                    new_value = value * neighbour_value
                    if neighbour not in visited:
                        queue.append((neighbour, new_value))
                        visited.add(neighbour)

                    if neighbour == target:
                        answer = new_value
                        break

            answers.append(answer)

        return answers


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        ),
        (
            [["a", "b"], ["b", "c"], ["bc", "cd"]],
            [1.5, 2.5, 5.0],
            [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
        ),
        ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]),
        (
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [
                ["x1", "x5"],
                ["x5", "x2"],
                ["x2", "x4"],
                ["x2", "x2"],
                ["x2", "x9"],
                ["x9", "x9"],
            ],
        ),
    ]

    for equations, values, queries in q:
        for i in range(len(equations)):
            print(f"{equations[i][0]} -> {equations[i][1]} = {values[i]}")
        print("queries: ", queries)
        print()
        answer = solution.calcEquation(equations, values, queries)
        print("answer: ", answer)
        print("=====================")
        print()
