from typing import List


class Solution(object):
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)

        lows = [-2] * n

        def dfs(node: int, depth: int) -> int:
            if lows[node] >= 0:
                return lows[node]

            lows[node] = depth

            low_depth = n

            for neighbour in graph[node]:
                if lows[neighbour] == depth - 1:
                    continue

                neighbour_low = dfs(neighbour, depth + 1)

                if neighbour_low <= depth:
                    if [node, neighbour] in connections:
                        connections.remove([node, neighbour])
                    if [neighbour, node] in connections:
                        connections.remove([neighbour, node])

                low_depth = min(low_depth, neighbour_low)

            return low_depth

        dfs(0, 0)

        return connections


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1], [1, 2], [2, 0], [1, 3]]),
        (2, [[0, 1]]),
        (13, [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 7], [7, 6], [6, 5], [5, 4]]),
    ]

    for n, connections in q:
        print("n: ", n)
        for a, b in connections:
            print(a, b)
        print()
        answer = solution.criticalConnections(n, connections)
        print("answer: ", answer)
        print("=====================")
        print()
