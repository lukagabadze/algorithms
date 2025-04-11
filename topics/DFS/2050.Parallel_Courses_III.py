from typing import List


"""
TIME: 280ms (Beats 6.21%)
It's slow, but I am proud since it is MY solution. I believe I can improve this a LOT before I peek into the solutions tab.
"""


class Solution(object):
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        for s, e in relations:
            s = s - 1
            e = e - 1
            graph[s].append(e)
            reverse_graph[e].append(s)

        min_times = [float("inf")] * n

        def dfs(node: int):
            if min_times[node] != float("inf"):
                return min_times[node]

            if not reverse_graph[node]:
                return time[node]

            node_time = (
                max(dfs(neighbour) for neighbour in reverse_graph[node]) + time[node]
            )
            min_times[node] = node_time
            return node_time

        # Alphas are the lonely nodes, they don't go anywhere.
        # Nodes come to them, but they don't have anywhere to go... poor alphas ✊😔
        alphas = [node for node in range(n) if not graph[node]]
        answer = 0
        for node in alphas:
            answer = max(answer, dfs(node))

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        (3, [[1, 3], [2, 3]], [3, 2, 5]),
        (5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]),
        (5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 1, 1, 4, 5]),
        (5, [[1, 4], [3, 4], [5, 4]], [6, 8, 1, 2, 1]),
    ]

    for n, relations, time in q:
        print("n: ", n)
        for s, e in relations:
            print(s - 1, e - 1)
        print("time: ", time)
        print()
        answer = solution.minimumTime(n, relations, time)
        print("answer: ", answer)
        print("=====================")
        print()
