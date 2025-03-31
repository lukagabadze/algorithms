from heapq import heappop, heappush
from typing import List
from collections import defaultdict


class Solution(object):
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, e, t in roads:
            graph[s].append((e, t))
            graph[e].append((s, t))

        heap = [(0, 0)]
        distances = defaultdict(lambda: float("inf"))
        answers = defaultdict(int)
        answers[0] = 1
        while heap:
            time, node = heappop(heap)

            for neighbour, neighbour_time in graph[node]:
                new_time = time + neighbour_time
                if new_time < distances[neighbour]:
                    heappush(heap, (new_time, neighbour))
                    distances[neighbour] = new_time

                if new_time == distances[neighbour]:
                    answers[neighbour] = (answers[neighbour] + answers[node]) % (
                        10**9 + 7
                    )

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
    ]

    for n, roads in q:
        print("n: ", n)
        print(*roads, sep="\n")
        print()
        answer = solution.countPaths(n, roads)
        print("answer: ", answer)
        print("=====================")
        print()
