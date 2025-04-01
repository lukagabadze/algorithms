"""
NOTE: Wow! Yesterday I was getting Wrong Answer and today it got accepted by just adding one line:
    answers[neighbour] = 0

This goes back to me not fully understanding how Dijkstra works. Do I go through the same node twice? How? Priority queue should be handling that.
In this problem, my wrong answer was higher than the actual answer, so that suggested to me that I was adding up unneeded values.

NOTE: I only push the node in my heap if going there improves my time (distance).
But my heap is sorted, so lowest distances will come first, the distances dictionary is filled with float('inf').
How is it possible that I go through the same node twice? Is that even what happens here??? (I am hella confused).
TODO: Figure this shit out, the question appears on the third test case in my array of questions at the bottom.

NOTE: Before I dive deep into Dijsktra, I want to share a small find:
ARRAYS ARE MUCH FASTER THAN DICTIONARIES.
I have heard this before, and now I see it with my own eyes.
Switching the graph, distances and answers for arrays instead of `defaultdict` made my solution 33% faster!
"""

from heapq import heappop, heappush
from typing import List


"""
TIME: 24ms (Beats 25.42%)
MEM: 25.18MB (Beats 41.15%)
NOTE: This is with dictionaries (graph, distances, answers)

TIME: 16ms (Beats 77.42%)
MEM: 25.00MB (Beats 82.96%)
NOTE: Now THIS is with arrays (graph, distances, answers), good shit!

NOTE: Arrays > Dictionaries
"""


class Solution(object):
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for s, e, t in roads:
            graph[s].append((e, t))
            graph[e].append((s, t))

        heap = [(0, 0)]
        distances = [float("inf")] * n
        answers = [0] * n
        answers[0] = 1
        while heap:
            time, node = heappop(heap)

            for neighbour, neighbour_time in graph[node]:
                new_time = time + neighbour_time

                if new_time < distances[neighbour]:
                    heappush(heap, (new_time, neighbour))
                    distances[neighbour] = new_time
                    answers[neighbour] = 0

                if new_time == distances[neighbour]:
                    answers[neighbour] = (answers[neighbour] + answers[node]) % MOD

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
