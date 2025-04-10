from typing import List
from heapq import heappop, heappush


class Solution(object):
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        for s, e in relations:
            s = s - 1
            e = e - 1
            graph[s].append(e)
            reverse_graph[e].append(s)

        leafs = []
        for i in range(n):
            if not reverse_graph[i]:
                heappush(leafs, (time[i], i, 0))

        answer = 0
        while leafs:
            if not leafs:
                return

            _, node, start_time = heappop(leafs)

            answer += max(start_time - answer + time[node], 0)
            reverse_graph[node] = "asd"

            for neighbour in graph[node]:
                reverse_graph[neighbour].remove(node)

                if not reverse_graph[neighbour]:
                    heappush(leafs, (time[neighbour], neighbour, answer))

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
