from typing import List
from heapq import heappop, heappush


"""
NOTE: I am fucking stupid, in the first test case you can't take course 4 without taking the 2,
my code takes courses 2 and 4 in the same semester, sorry for this bad submission 😔
"""


class Solution(object):
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        for s, e in relations:
            s = s - 1
            e = e - 1
            graph[s].append(e)
            reverse_graph[e].append(s)

        # Initialize the heap with the starting points
        heap = []
        for i in range(n):
            if not reverse_graph[i]:
                # (courses_taken, node)
                heappush(heap, (0, i))

        semesters = [k] * n * k
        current_semester = 0

        def process_semester():
            nonlocal current_semester
            if semesters[current_semester] <= 0:
                current_semester += 1

            semesters[current_semester] -= 1

        visited = set()
        while heap:
            (courses_taken, node) = heappop(heap)

            if courses_taken == 0:
                process_semester()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    heappush(heap, ((courses_taken + 1) % k, neighbour))
                    visited.add(neighbour)

        return sum(1 for item in semesters if item < k)


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
