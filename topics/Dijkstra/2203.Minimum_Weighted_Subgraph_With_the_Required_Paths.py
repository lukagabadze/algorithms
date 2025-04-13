from heapq import heappop, heappush
from collections import defaultdict
from typing import List


class Solution(object):
    def minimumWeight(
        self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int
    ) -> int:
        graph = [[] for _ in range(n)]
        weights = defaultdict(int)
        for node1, node2, weight in edges:
            graph[node1].append(node2)

            if weights[(node1, node2)] == 0:
                weights[(node1, node2)] = weight
            else:
                weights[(node1, node2)] = min(weight, weights[(node1, node2)])

        def find_min_path(source: int, destination: int):
            # (weight, node)
            heap = [(0, source)]
            min_weights = [float("inf")] * n
            parents = [-1] * n
            while heap:
                weight, node = heappop(heap)

                for neighbour in graph[node]:
                    new_weight = weight + weights[(node, neighbour)]
                    if new_weight < min_weights[neighbour]:
                        heappush(heap, (new_weight, neighbour))
                        min_weights[neighbour] = new_weight
                        parents[neighbour] = node

            return (min_weights[destination], parents)

        possibilites = [
            [src1, dest, src2, dest],
            [src2, dest, src1, dest],
        ]
        answer = float("inf")
        for node1, node2, node3, node4 in possibilites:
            weights_bak = dict(weights)

            (path1, parents) = find_min_path(node1, node2)

            node = node2
            while node != node1 and parents[node] != -1:
                weights[parents[node], node] = 0
                node = parents[node]

            (path2, parents) = find_min_path(node3, node4)

            answer = min(answer, path1 + path2)

            weights = dict(weights_bak)

        if answer == float("inf"):
            return -1

        return answer


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
