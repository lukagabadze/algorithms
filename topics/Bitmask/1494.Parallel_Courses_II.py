"""
NOTE: I would NEVER be able to solve this on my own. I did reach the realisation that I would need bitmasks,
since n <= 15, but I would never figure this out.

NOTE: HUGE thanks to hxu10 (https://leetcode.com/problems/parallel-courses-ii/solutions/708359/python-bitmask-and-bfs).
The solution is clean, simple and super fast.

NOTE: Without the answers array where you keep minimum steps required to reach a certain bitmask,
the solution is slow, but when you add that answers array and only push to the queue when it improves your steps, it becomes BLAZING fast.
This is generally the case with BFS, it's like having a visited set in graphs.
"""

from typing import List
from collections import deque
from itertools import combinations


"""
TIME: 296ms (Beats 87.64%)
MEMORY: 19.12MB (Beats 62.99%)
NOTE: Massive thanks to the GOAT hxu10!
"""


class Solution(object):
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        relations = [[s - 1, e - 1] for s, e in relations]
        target = (1 << n) - 1

        # Create dependency array.
        # dep[i] bitmask indicates that to take lecture i
        # you need to have all the lectures of dep[i] bitmask taken.
        # Example: dp[3] = 0110 means that to take lecture 3 you need to have lecture 1 and lecture 2 already taken.
        dep = [0] * n
        for s, e in relations:
            dep[e] = dep[e] | (1 << s)

        queue = deque([(0, 0)])
        answers = [float("inf")] * (1 << n)
        while queue:
            mask, step = queue.popleft()

            next_nodes = []
            for i in range(n):
                # If prerequisites of the node i are met
                # And, the node i is NOT already included in our mask
                # push it to the next_nodes array
                if dep[i] & mask == dep[i] and (1 << i) & mask == 0:
                    next_nodes.append(i)

            # If next_nodes are lower than the limit, combine it and push it.
            if len(next_nodes) <= k:
                for node in next_nodes:
                    mask |= 1 << node

                if mask == target:
                    return step + 1

                if step + 1 < answers[mask]:
                    queue.append((mask, step + 1))
                    answers[mask] = step + 1

            # If next_nodes array is bigger than the limit
            # we need to find all the ways to combine the nodes
            # in the k limit and push them one by one in the queue
            # to try all the possible ways.
            if len(next_nodes) > k:
                for nodes_combination in list(combinations(next_nodes, k)):
                    new_mask = mask
                    for node in nodes_combination:
                        new_mask |= 1 << node

                    if step + 1 < answers[new_mask]:
                        queue.append((new_mask, step + 1))
                        answers[new_mask] = step + 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[2, 1], [3, 1], [1, 4]], 2),
        (5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2),
        (11, [], 2),
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
