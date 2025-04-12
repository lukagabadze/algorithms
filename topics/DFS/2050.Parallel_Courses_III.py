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


NOTE: reverse_graph was a LIE.
you get the same result by using just the normal adjacency graph 😁
Ony leetcode user mentioned it in the comments and I investigated it a little bit, here is my explanation:
https://leetcode.com/problems/parallel-courses-iii/solutions/4180303/98-44-easy-solution-with-explanation/comments/2943814/?parent=2729304
"""

from typing import List


"""
TIME: 280ms (Beats 6.21%)
NOTE: It's slow, but I am proud since it is MY solution. I believe I can improve this a LOT before I peek into the solutions tab.

TIME: 187ms (Beats 24.75%)
MEMORY: 117MB (Beats 5.01%)
NOTE: I removed the graph array. It was only used to find the "alphas" the lonely nodes.
But, you can reach the same result by just going through all the nodes and running dfs with caching.
Speaking of caching, the reason why the memory result is so dogshit, is because I use @cache from functools.
I will swich back to min_times array for caching and see the results.

TIME: 170ms (Beats 32.65%)
Memory: 91.42MB (Beats 5.01%)
NOTE: I did what I said I would do, but did not get the greatest results.
It's an improvement, but not good enough.
"""


class Solution(object):
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for s, e in relations:
            graph[e - 1].append(s - 1)

        min_times = [-1] * n

        def dfs(node: int):
            if min_times[node] != -1:
                return min_times[node]

            if not graph[node]:
                min_times[node] = time[node]
                return min_times[node]

            time_took = max(dfs(neighbour) for neighbour in graph[node]) + time[node]
            min_times[node] = time_took

            return min_times[node]

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
