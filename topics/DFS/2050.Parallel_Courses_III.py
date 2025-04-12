"""
NOTE: Two different caching methods inside my dfs have the same result in time, but very different in memory consumption.
The first method was to use an array:

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


I would save the results inside the `min_times` array and the results were:
TIME: 280ms
MEMORY: 98MB


Then I went ahead and used @cache from functools:

        @cache
        def dfs(node: int):
            if not reverse_graph[node]:
                return time[node]

            return max(dfs(neighbour) for neighbour in reverse_graph[node]) + time[node]


The code looks much cleaner, much simpler, but, the results are not as good.
TIME: 279ms
MEMORY: 123.9MB

We saved 1ms but at the cost of 25.9MB of memory, not good imo.
But for code readability, i think it's good.
"""

from typing import List
from functools import cache


"""
TIME: 280ms (Beats 6.21%)
NOTE: It's slow, but I am proud since it is MY solution. I believe I can improve this a LOT before I peek into the solutions tab.

TIME: 187ms (Beats 24.75%)
MEMORY: 117MB (Beats 5.01%)
NOTE: I removed the graph array. It was only used to find the "alphas" the lonely nodes.
But, you can reach the same result by just going through all the nodes and running dfs with caching.
Speaking of caching, the reason why the memory result is so dogshit, is because I use @cache from functools.
I will swich back to min_times array for caching and see the results.
"""


class Solution(object):
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        reverse_graph = [[] for _ in range(n)]
        for s, e in relations:
            reverse_graph[e - 1].append(s - 1)

        @cache
        def dfs(node: int):
            if not reverse_graph[node]:
                return time[node]

            return max(dfs(neighbour) for neighbour in reverse_graph[node]) + time[node]

        answer = 0
        for node in range(n):
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
