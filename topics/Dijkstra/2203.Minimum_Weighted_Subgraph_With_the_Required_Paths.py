"""
NOTE: Huge thanks to the GOAT shrok.
He came up with a solution of just running one Dijkstra and leaving a trail so to speak to find an answer.
(https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/solutions/1844479/simultaneous-dijkstra-beats-100-only-1-dijkstra)

NOTE: The code is very different from the solution, I put the node type logic inside the neighbour for loop.
So I had to adapt the code for it to pass.
You can also do it the other way around (have the neighbour for loop inside each node type logic), just like shrok's solution,
but I just started writing the solution on my own and found myself trying to solve it like this.

NOTE: The final nail in the coffin to solve this problem was to slightly change the node type logic.
If the code saw you could go from node_type 1 to node_type 3 it would take it immediately and never consider
staying on the node_type 1 route.
Now, instead of having if and elif, I just have 2 ifs.
This way, we consider both node_type 3 and node_type 1 routes.
"""

from heapq import heappop, heappush
from typing import List


"""
TIME: 718ms (Beats 82.44%)
MEMORY: 75.38MB (Beats 97.55%)
"""


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
        min_weights_1 = [float("inf")] * n
        min_weights_1[src1] = 0
        min_weights_2 = [float("inf")] * n
        min_weights_2[src2] = 0
        min_weights = [float("inf")] * n

        while heap:
            weight, node, node_type = heappop(heap)

            if node == dest and node_type == NodeType.both:
                return weight

            for neighbour, neighbour_weight in graph[node]:
                new_weight = weight + neighbour_weight

                # NodeType.first
                if node_type == NodeType.first:
                    possible_type_three_weight = new_weight + min_weights_2[neighbour]

                    # If NodeType.second has already been here and going to the neighbour as NodeType.both is benefitial,
                    # continue as NodeType.both, otherwise, just continue as NodeType.first
                    if (
                        min_weights_2[neighbour] != float("inf")
                        and possible_type_three_weight < min_weights[neighbour]
                    ):
                        heappush(
                            heap,
                            (
                                possible_type_three_weight,
                                neighbour,
                                NodeType.both,
                            ),
                        )
                        min_weights[neighbour] = possible_type_three_weight

                    if new_weight < min_weights_1[neighbour]:
                        heappush(heap, (new_weight, neighbour, NodeType.first))
                        min_weights_1[neighbour] = new_weight

                # NodeType.second
                if node_type == NodeType.second:
                    possible_type_three_weight = new_weight + min_weights_1[neighbour]

                    # Same here, if NodeType.first has already been here and going to the neighbour as NodeType.both is benefitial,
                    # continue as NodeType.both, otherwise, just continue as NodeType.second
                    if (
                        min_weights_1[neighbour] != float("inf")
                        and possible_type_three_weight < min_weights[neighbour]
                    ):
                        heappush(
                            heap,
                            (
                                possible_type_three_weight,
                                neighbour,
                                NodeType.both,
                            ),
                        )
                        min_weights[neighbour] = possible_type_three_weight

                    if new_weight < min_weights_2[neighbour]:
                        heappush(heap, (new_weight, neighbour, NodeType.second))
                        min_weights_2[neighbour] = new_weight

                # NodeType.both
                if node_type == NodeType.both:
                    if new_weight < min_weights[neighbour]:
                        heappush(heap, (new_weight, neighbour, NodeType.both))
                        min_weights[neighbour] = new_weight

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
        # Same as the previous one, but longer 0->1 weight comes first
        (
            5,
            [[4, 2, 20], [4, 3, 46], [0, 1, 43], [0, 1, 15], [0, 1, 32], [3, 1, 13]],
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
