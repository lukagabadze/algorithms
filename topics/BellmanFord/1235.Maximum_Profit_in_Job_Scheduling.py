"""
NOTE: Funny thing:
    graph = [[]] * n

This does NOT work AT ALL.
When you push one element in the 0th array, it pushet it to all (object referrences baby).
The correct way to code this would be:
    graph = [[] for _ in range(n)]

"""

from typing import List


class Solution(object):
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        for s, e in relations:
            s = s - 1
            e = e - 1
            graph[e].append(s)

        answers = [k - 1] * n
        for _ in range(n):
            for node in range(n):
                for neighbour in graph[node]:
                    if answers[neighbour] > 0:
                        if answers[node] == k - 1:
                            answers[node] = answers[neighbour] - 1
                        else:
                            answers[node] = max(answers[node], answers[neighbour] - 1)

        return sum(answers)


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[2, 1], [3, 1], [1, 4]], 2),
        (5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2),
    ]

    for n, relations, k in q:
        print("n: ", n)
        print(*relations, sep="\n")
        print("k: ", k)
        print()
        answer = solution.minNumberOfSemesters(n, relations, k)
        print("answer: ", answer)
        print("=====================")
        print()
