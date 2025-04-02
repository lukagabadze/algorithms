"""
NOTE: I'm trying to solve this using Bellman-Ford algorithm.
I have a very good feeling that this could work well.
"""

from typing import List


class Solution(object):
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for s, e, t in roads:
            graph[s].append((e, t))
            graph[e].append((s, t))

        times = [float("inf")] * n
        times[0] = 0
        answers = [(0, set())] * n
        answers[0] = (1, set())
        for _ in range(n):
            for node in range(n):
                for neighbour, time in graph[node]:
                    new_time = times[node] + time

                    if new_time < times[neighbour]:
                        times[neighbour] = new_time
                        answers[neighbour] = (0, set())

                    if (
                        new_time == times[neighbour]
                        and new_time != float("inf")
                        and node not in answers[neighbour][1]
                    ):
                        answers[neighbour] = (
                            (answers[neighbour][0] + answers[node][0]) % MOD,
                            answers[neighbour][1] | set([node]),
                        )

        return answers[n - 1][0]


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
