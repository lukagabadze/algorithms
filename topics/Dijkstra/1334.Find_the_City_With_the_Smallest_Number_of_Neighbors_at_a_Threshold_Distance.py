from heapq import heappop, heappush
from typing import List


"""
TIME: 163ms (Beats 86.70%)
NOTE: Took me like 15 minutes to solve and it passed on the first try... I AM FUCKING GOATED!!!
"""


class Solution(object):
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for s, e, d in edges:
            graph[s].append((e, d))
            graph[e].append((s, d))

        answer = (0, float("inf"))
        for i in range(n):
            # (distance, node)
            heap = [(0, i)]
            distances = [float("inf")] * n
            distances[i] = 0
            nodes_reached = 0
            while heap:
                distance, node = heappop(heap)

                for neighbour, neighbour_distance in graph[node]:
                    new_distance = distance + neighbour_distance
                    if (
                        new_distance < distances[neighbour]
                        and new_distance <= distanceThreshold
                    ):
                        heappush(heap, (new_distance, neighbour))

                        if distances[neighbour] == float("inf"):
                            nodes_reached += 1

                        distances[neighbour] = new_distance

            if nodes_reached <= answer[1]:
                answer = (i, nodes_reached)

        return answer[0]


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4),
        (5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2),
    ]

    for n, edges, distanceThreshold in q:
        print("n: ", n)
        for i, row in enumerate(edges):
            print(f"{i}: {row}")
        print()
        answer = solution.findTheCity(n, edges, distanceThreshold)
        print("answer: ", answer)
        print("=====================")
        print()
