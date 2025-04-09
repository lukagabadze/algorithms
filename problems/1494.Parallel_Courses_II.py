"""
NOTE: This solution gets wrong answer on testcase 67/82 and I know why.
it has one small issue, when I find the leafs and cut off the last bit in the end if len(leafs) > k,
I don't choose which leafs I should keep and which ones to cut off. There might be a better way to choose leafs to free up some other nodes for the future.
I just don't know how to do it yet.

NOTE: I updated the code and added node prioritization logic and it was a very very very solid solution.
But it still fails... This time on testcase 75/82 (last testcase in my code).

NOTE: I solved it using bitmasks, you can check it out inside the topics/Bitmask folder.
I will still keep this because I really do believe this was a solid attempt by me.
"""

from typing import List


"""
NOTE: DOES NOT WORK, WRONG ANSWER ON 75/82
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

        answer = 0
        visited = set()
        for _ in range(n):
            leafs = [i for i in range(n) if not reverse_graph[i] and i not in visited]

            if len(leafs) == 0:
                break

            def sort_key(x):
                neighbors = graph[x]
                if not neighbors:
                    return float("inf")

                return min((len(reverse_graph[i]) for i in graph[x]))

            # Sort the leafs in a way where we prioritize the nodes which complete some other nodes
            # requirements so we can process that one as well as soon as possible.
            leafs = sorted(
                leafs,
                key=sort_key,
            )

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
        (
            13,
            [
                [12, 8],
                [2, 4],
                [3, 7],
                [6, 8],
                [11, 8],
                [9, 4],
                [9, 7],
                [12, 4],
                [11, 4],
                [6, 4],
                [1, 4],
                [10, 7],
                [10, 4],
                [1, 7],
                [1, 8],
                [2, 7],
                [8, 4],
                [10, 8],
                [12, 7],
                [5, 4],
                [3, 4],
                [11, 7],
                [7, 4],
                [13, 4],
                [9, 8],
                [13, 8],
            ],
            9,
        ),
        (
            12,
            [
                [1, 2],
                [1, 3],
                [7, 5],
                [7, 6],
                [4, 8],
                [8, 9],
                [9, 10],
                [10, 11],
                [11, 12],
            ],
            2,
        ),
    ]

    for n, relations, k in q:
        print("n: ", n)
        for s, e in relations:
            print(s - 1, e - 1)
        print("k: ", k)
        print()
        answer = solution.minNumberOfSemesters(n, relations, k)
        print("answer: ", answer)
        print("=====================")
        print()
