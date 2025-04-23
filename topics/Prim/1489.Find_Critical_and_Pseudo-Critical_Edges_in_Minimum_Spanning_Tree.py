from typing import List
from heapq import heappush, heappop


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        E = len(edges)

        if E == 1:
            return [[0], []]

        graph = [[] for _ in range(n)]
        for i, (s, e, w) in enumerate(edges):
            graph[s].append((e, w, i))
            graph[e].append((s, w, i))

        min_total_weights = []
        for i, (node1, node2, _) in enumerate(edges):
            for start_node in range(n):
                heap = [(0, start_node)]
                total_weight = 0
                visited = set()
                while heap:
                    weight, node = heappop(heap)

                    if node in visited:
                        continue

                    visited.add(node)
                    total_weight += weight

                    for neighbour, neighbour_weight, _ in graph[node]:
                        # Skip the selected edge
                        if min(node, neighbour) == min(node1, node2) and max(
                            node, neighbour
                        ) == max(node1, node2):
                            continue

                        if neighbour not in visited:
                            heappush(heap, (neighbour_weight, neighbour))

            if len(visited) != n:
                min_total_weights.append(float("inf"))
            else:
                min_total_weights.append(total_weight)

        critical_nodes = [
            i
            for i, val in enumerate(min_total_weights)
            if val != min(min_total_weights)
        ]

        occurrences = [0] * E
        min_total_weight = float("inf")
        for i, (node1, node2, weight) in enumerate(edges):
            heap = [(weight, (node1, node2), i)]
            visited = set()
            temp_ocurrences = [False] * E
            total_weight = 0
            while heap:
                weight, (node1, node2), edge_ind = heappop(heap)

                if node1 in visited and node2 in visited:
                    continue

                visited.add(node1)
                visited.add(node2)
                total_weight += weight

                temp_ocurrences[edge_ind] = True

                for neighbour, neighbour_weight, neighbour_edge_ind in graph[node1]:
                    if neighbour not in visited:
                        heappush(
                            heap,
                            (
                                neighbour_weight,
                                (node1, neighbour),
                                neighbour_edge_ind,
                            ),
                        )
                for neighbour, neighbour_weight, neighbour_edge_ind in graph[node2]:
                    if neighbour not in visited:
                        heappush(
                            heap,
                            (
                                neighbour_weight,
                                (node2, neighbour),
                                neighbour_edge_ind,
                            ),
                        )

            if total_weight < min_total_weight:
                occurrences = list(map(int, temp_ocurrences))
                min_total_weight = total_weight
            elif total_weight == min_total_weight:
                occurrences = [x + y for x, y in zip(occurrences, temp_ocurrences)]

        pseudo_critical_nodes = [
            i
            for i, val in enumerate(occurrences)
            if val != 0 and i not in critical_nodes
        ]

        return [critical_nodes, pseudo_critical_nodes]


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            5,
            [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
        ),
        (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]),
        (
            6,
            [
                [0, 1, 1],
                [1, 2, 1],
                [0, 2, 1],
                [2, 3, 4],
                [3, 4, 2],
                [3, 5, 2],
                [4, 5, 2],
            ],
        ),
        (2, [[0, 1, 3]]),
        (3, [[0, 1, 1], [0, 2, 2], [1, 2, 3]]),
    ]

    for n, edges in q:
        print("n: ", n)
        for row in edges:
            print(*row)
        print()
        answer = solution.findCriticalAndPseudoCriticalEdges(n, edges)
        print("answer: ", answer)
        print("=====================")
        print()
