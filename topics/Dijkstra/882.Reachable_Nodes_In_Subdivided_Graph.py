from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        distance_map = defaultdict(int)
        for node1, node2, sub_nodes in edges:
            graph[node1].append((node2, sub_nodes))
            graph[node2].append((node1, sub_nodes))
            distance_map[min(node1, node2), max(node1, node2)] = sub_nodes

        # Heap starting point (distance, node)
        heap = [(0, 0)]
        visited_paths = set()
        remainder_sub_nodes = 0
        while heap:
            distance, node = heappop(heap)

            if distance > maxMoves:
                break

            for neighbour, sub_nodes in graph[node]:
                new_distance = distance + sub_nodes + 1

                if (min(node, neighbour), max(node, neighbour)) not in visited_paths:
                    if new_distance <= maxMoves:
                        heappush(heap, (new_distance, neighbour))
                        visited_paths.add((min(node, neighbour), max(node, neighbour)))

                    if new_distance > maxMoves:
                        remainder_sub_nodes += maxMoves - distance

        answer = 0
        nodes_set = set()
        for node1, node2 in visited_paths:
            answer += distance_map[(node1, node2)]
            nodes_set.update([node1, node2])

        answer += len(nodes_set)
        answer += remainder_sub_nodes
        return answer or 1


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3),
        ([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4),
        ([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5),
    ]

    for edges, maxMoves, n in q:
        for row in edges:
            print(row)
        print("maxMoves: ", maxMoves)
        print("n: ", n)
        print()
        answer = solution.reachableNodes(edges, maxMoves, n)
        print("answer: ", answer)
        print("=====================")
        print()
