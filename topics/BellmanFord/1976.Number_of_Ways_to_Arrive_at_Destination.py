"""
NOTE: I'm trying to solve this using Bellman-Ford algorithm.
I have a very good feeling that this could work well.
"""

from typing import List


"""
TIME: 1208ms (Beats 5.01%)
NOTE: Yeah, Bellman-Ford does not do well here. I will try to improve on this but it does not look good so far.
I'm still glad I solved it using bellman-ford.
I also have a proper fast solution using Dijkstra's algorithm inside the Dijkstra folder.
"""


class Solution(object):
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for s, e, t in roads:
            graph[s].append((e, t))
            graph[e].append((s, t))

        times = [float("inf")] * n
        times[0] = 0
        answers = [0] * n
        answers[0] = 1
        for _ in range(n):
            new_answers = [0] * n
            new_answers[0] = 1

            for node in range(n):
                for neighbour, time in graph[node]:
                    new_time = times[node] + time

                    if new_time < times[neighbour]:
                        times[neighbour] = new_time
                        answers[neighbour] = 0

                    if new_time == times[neighbour] and new_time != float("inf"):
                        new_answers[neighbour] = (
                            new_answers[neighbour] + answers[node]
                        ) % MOD

            answers = list(new_answers)

        return answers[n - 1]


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            7,
            [
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
        ),
        (2, [[1, 0, 10]]),
        (
            6,
            [
                [0, 1, 5],
                [0, 2, 1],
                [1, 3, 1],
                [1, 5, 1],
                [2, 3, 2],
                [2, 4, 1],
                [3, 4, 1],
            ],
        ),
    ]

    for n, roads in q:
        print("n: ", n)
        print(*roads, sep="\n")
        print()
        answer = solution.countPaths(n, roads)
        print("answer: ", answer)
        print("=====================")
        print()
