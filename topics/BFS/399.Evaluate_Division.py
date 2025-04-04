"""
NOTE: I asked ChatGPT for problems that I would solve with Bellman-Ford and it gave me this.
It really does NOT need Bellman-Ford, not even Dijkstra, just plain old BFS.

NOTE: I had a piece of code that looked like this inside the graph creation logic:

            if len(a) > 1:
                for node in a:
                    graph[a].append((node, 1))
                    graph[node].append((a, 1))

            if len(b) > 1:
                for node in b:
                    graph[b].append((node, 1))
                    graph[node].append((b, 1))

This code took a node "bc" and created edges between "b" -> "bc" with weight of 1
and "c" -> "bc" with weight of 1.
Basically, took every character of the node and created links between it and the entire node.
I thought that made sence since if you have info that ab/cd and you have info individually on a, b, c and d
you might be able to piece them together to make up ab/cd.
But, I found out it had flaws, check my last testcase.
It went from x1 to x to 4 to x4 to x5. Which as you guessed, is hella incorrect.
But I am still wondering, how do you handle such case?
"""

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
