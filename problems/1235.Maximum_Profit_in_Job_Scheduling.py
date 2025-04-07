"""
NOTE: This solution gets wrong answer on testcase 67/82 and I know why.
it has one small issue, when I find the leafs and cut off the last bit in the end if len(leafs) > k,
I don't choose which leafs I should keep and which ones to cut off. There might be a better way to choose leafs to free up some other nodes for the future.
I just don't know how to do it yet.
"""

from typing import List


class Solution(object):
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        n = n
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        for s, e in relations:
            s = s - 1
            e = e - 1
            graph[s].append(e)
            reverse_graph[e].append(s)

        answer = 0
        visited = set()
        for _ in range(n):
            leafs = [i for i in range(n) if not reverse_graph[i] and i not in visited]

            if len(leafs) == 0:
                break

            if len(leafs) > k:
                answer += len(leafs) // k
                leafs = leafs[: len(leafs) - len(leafs) % k]
            else:
                answer += 1

            for i in leafs:
                visited.add(i)
                for node in graph[i]:
                    if i in reverse_graph[node]:
                        reverse_graph[node].remove(i)

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[2, 1], [3, 1], [1, 4]], 2),
        (5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2),
        (11, [], 2),
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
