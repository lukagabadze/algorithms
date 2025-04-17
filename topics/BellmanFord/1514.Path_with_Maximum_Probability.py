"""
NOTE: Just using Bellman-Ford without any improvements gets TLE:
        probs = [0] * n
        probs[start_node] = 1
        for _ in range(n):
            for i, (node1, node2) in enumerate(edges):
                probs[node2] = max(probs[node2], probs[node1] * succProb[i])
                probs[node1] = max(probs[node1], probs[node2] * succProb[i])

        return probs[end_node]

This is the cutest piece of code I have ever seen. It's slow as shit, but cute!


NOTE: By adding the `finished` boolean variable to check if
every maximum probability has been calculated made this solution pass.
And it passed with better results than I initially imagined.
I think that's because there is a lack of testcases against this method.
On Codeforces, O(10^8) would never fly imo. But I would love to be wrong on that claim.

NOTE: Funny thing, this slow solution has better performance on leetcode than my initial Dijkstra...
Fuck you, it was one my first times solving with Dijkstra.

NOTE: Also something important to note, the MEMORY on this solution is better than 99.52% of the solutions.
So if your problem requires memory improvements at the cost of time, Bellman-Ford is your man.
"""

from typing import List


"""
TIME: 144ms (Beats 21.48%)
MEMORY: 25.97MB (Beats 99.52%) WOW
"""


class Solution(object):
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        probs = [0] * n
        probs[start_node] = 1
        for j in range(n):
            finished = True
            for i, (node1, node2) in enumerate(edges):
                if probs[node1] * succProb[i] > probs[node2]:
                    probs[node2] = probs[node1] * succProb[i]
                    finished = False

                if probs[node2] * succProb[i] > probs[node1]:
                    probs[node1] = probs[node2] * succProb[i]
                    finished = False

            # Don't continue if none of the Nodes have improved their probability,
            # because nothing will change from this point, we found maximum probabilities to every node.
            if finished:
                break

        return probs[end_node]


if __name__ == "__main__":
    solution = Solution()

    q = [
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),
        (
            5,
            [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
            [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
            3,
            4,
        ),
        (3, [[0, 1]], [0.5], 0, 2),
    ]

    for n, edges, succProb, start, end in q:
        print("n: ", n)
        print("edges: ", edges)
        print("succProb: ", succProb)
        print("start: ", start)
        print("end: ", end)
        answer = solution.maxProbability(n, edges, succProb, start, end)
        print("answer: ", answer)
        print()
