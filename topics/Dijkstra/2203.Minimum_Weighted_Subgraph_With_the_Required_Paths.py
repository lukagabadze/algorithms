from heapq import heappop, heappush
from typing import List


class Solution(object):
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for node1, node2, weight in edges:
            graph[node1].append((node2, weight))

        class NodeType:
            first = 1
            second = 2
            both = 3

        # (weight, node, type)
        heap = [
            (0, src1, NodeType.first),
            (0, src2, NodeType.second),
        ]

        min_weights_1 = [-1] * n
        min_weights_1[src1] = 0

        min_weights_2 = [-1] * n
        min_weights_2[src2] = 0

        min_weights = [-1] * n
        while heap:
            weight, node, node_type = heappop(heap)

            for neighbour, neighbour_weight in graph[node]:
                new_weight = weight + neighbour_weight

                # NodeType.first
                if node_type == NodeType.first:
                    if min_weights_1[neighbour] != -1:
                        continue

                    # If NodeType.second has already been here, continue as NodeType.both
                    # Otherwise, just continue NodeType.first
                    if min_weights_2[neighbour] != -1:
                        new_weight = (
                            min_weights_2[neighbour] + weight + neighbour_weight
                        )
                        heappush(heap, (new_weight, node, NodeType.both))
                        min_weights[neighbour] = new_weight
                    else:
                        heappush(heap, (new_weight, neighbour, NodeType.first))
                        min_weights_1[neighbour] = new_weight

                # NodeType.second
                if node_type == NodeType.second:
                    if min_weights_2[neighbour] != -1:
                        continue

                    # If NodeType.first has already been here, continue as NodeType.both
                    # Otherwise, just continue NodeType.second
                    if min_weights_1[neighbour] != -1:
                        new_weight = (
                            min_weights_1[neighbour] + weight + neighbour_weight
                        )
                        heappush(heap, (new_weight, node, NodeType.both))
                        min_weights[neighbour] = new_weight
                    else:
                        heappush(heap, (new_weight, neighbour, NodeType.second))
                        min_weights_2[neighbour] = new_weight

                # NodeType.both
                if node_type == NodeType.both:
                    if neighbour == dest:
                        return new_weight

                    if min_weights[neighbour] != -1:
                        continue

                    min_weights[neighbour] = new_weight

                    heappush(heap, (new_weight, neighbour, NodeType.both))

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            6,
            [
                [0, 2, 2],
                [0, 5, 6],
                [1, 0, 3],
                [1, 4, 5],
                [2, 1, 1],
                [2, 3, 3],
                [2, 3, 4],
                [3, 4, 2],
                [4, 5, 1],
            ],
            0,
            1,
            5,
        ),
        (3, [[0, 1, 1], [2, 1, 1]], 0, 1, 2),
        (
            5,
            [[0, 2, 1], [0, 3, 1], [2, 4, 1], [3, 4, 1], [1, 2, 1], [1, 3, 10]],
            0,
            1,
            4,
        ),
        (
            5,
            [[4, 2, 20], [4, 3, 46], [0, 1, 15], [0, 1, 43], [0, 1, 32], [3, 1, 13]],
            0,
            4,
            1,
        ),
        (3, [[0, 2, 10], [1, 2, 10], [1, 0, 1]], 0, 1, 2),
        (
            6,
            [
                [0, 2, 10],
                [0, 4, 2],
                [1, 4, 2],
                [1, 3, 10],
                [3, 5, 10],
                [4, 5, 20],
                [2, 5, 10],
            ],
            0,
            1,
            5,
        ),
    ]

    for n, edges, src1, src2, dest in q:
        print("n: ", n)
        for s, e, w in edges:
            print(s, e, w)
        print("src1: ", src1)
        print("src2: ", src2)
        print("dest: ", dest)
        print()
        answer = solution.minimumWeight(n, edges, src1, src2, dest)
        print("answer: ", answer)
        print("=====================")
        print()
