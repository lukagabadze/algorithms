"""
NOTE: Thanks again to Sung Jinwoo!
(https://leetcode.com/problems/largest-color-value-in-a-directed-graph/solutions/6781399/using-dfs-c-python-java)

NOTE: This problem showcases how to detect cycles in a directed graph.
And not only that, but how to solve graph problems using DFS and few markers (0, 1, 2 -> not visited, visiting, visited)
"""

from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        colors = [ord(c) - ord("a") for c in colors]
        n = len(colors)
        INF = float("inf")

        graph = [[] for _ in range(n)]
        for s, e in edges:
            graph[s].append(e)

        count = [[0] * 26 for _ in range(n)]

        # Visited can have 3 values:
        # 0 - Unexplored
        # 1 - Visiting (visit in progress by some other node)
        # 2 - Visited (visit done)
        visited = [0] * n

        def dfs(node: int) -> int:
            # If some other node is visiting this node
            # and we stumble upon it that means we have a FUCKING CYCLE BITCH
            if visited[node] == 1:
                return INF

            if visited[node] == 2:
                return count[node][colors[node]]

            # Start the visiting procedure and run recursive dfs from this node
            visited[node] = 1
            for neighbour in graph[node]:
                res = dfs(neighbour)

                # If a cycle has been detected, return straight away
                if res == INF:
                    return INF

                # Update the node value with the finished neighbour values
                for c in range(26):
                    count[node][c] = max(count[node][c], count[neighbour][c])

            count[node][colors[node]] += 1

            # Mark the node as visited
            visited[node] = 2

            return count[node][colors[node]]

        # Run the dfs from every node and record the max answer
        answer = 0
        for node in range(n):
            res = dfs(node)

            # If it returns INF that means a cycle has been detected in this directed graph
            if res == INF:
                return -1

            answer = max(answer, res)

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]),
        ("a", [[0, 0]]),
        ("abacab", [[0, 1], [0, 2], [2, 3], [3, 4], [4, 1]]),
    ]

    for colors, edges in q:
        print("colors: ", colors)
        print("edges: ", edges)
        print()
        answer = solution.largestPathValue(colors, edges)
        print("answer: ", answer)
        print("=====================")
        print()
