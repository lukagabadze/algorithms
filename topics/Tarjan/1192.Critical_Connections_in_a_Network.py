"""
NOTE: Important thing to note here is that the solution does not work if you don't change the connections array to a set.
If you don't change it, removing an element from that array takes O(n) time, while with sets it takes O(1).

So this two lines are important:
    1) connections = set(map(tuple, map(sorted, connections)))
    2) connections.remove(tuple(sorted((node, neighbour))))


NOTE: A funny thing to note is that I am not returning List[List[int]], I am returning List[Tuple[int]].
Like so: [(3, 4), (2, 3)], when the output should be [[3, 4], [2, 3]].
But leetcode does not bitch about it, it takes both answers.
"""

from typing import List


"""
TIME: 379ms (Beats 22.30%)
NOTE: MASSIVE thanks to Kaiwen Sun for the amazing explanation!
(https://leetcode.com/problems/critical-connections-in-a-network/solutions/382638/dfs-detailed-explanation-o-e-solution)
"""


class Solution(object):
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)

        lows = [-2] * n
        connections = set(map(tuple, map(sorted, connections)))

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
                    connections.remove(tuple(sorted((node, neighbour))))

                low_depth = min(low_depth, neighbour_low)

            return low_depth

        dfs(0, 0)
        return list(connections)


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
