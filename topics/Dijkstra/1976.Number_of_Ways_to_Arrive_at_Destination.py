"""
NOTE: Wow! Yesterday I was getting Wrong Answer and today it got accepted by just adding one line:
    answers[neighbour] = 0

This goes back to me not fully understanding how Dijkstra works. Do I go through the same node twice? How? Priority queue should be handling that.
In this problem, my wrong answer was higher than the actual answer, so that suggested to me that I was adding up unneeded values.

NOTE: I only push the node in my heap if going there improves my time (distance).
But my heap is sorted, so lowest distances will come first, the distances dictionary is filled with float('inf').
How is it possible that I go through the same node twice? Is that even what happens here??? (I am hella confused).

NOTE: Before I dive deep into Dijsktra, I want to share a small find:
ARRAYS ARE MUCH FASTER THAN DICTIONARIES.
I have heard this before, and now I see it with my own eyes.
Switching the graph, distances and answers for arrays instead of `defaultdict` made my solution 33% faster!

NOTE: I have figured out why we need to assign the distances inside the `if new_time < distances[neighbour]` statement:
Assigning the distances inside or outside the if statement will give you the same result if you just want to know the minimum distance.
BUT, in this problem we need to find all the possible paths to n-1 node, so we might (not might, absolutely) have to visit the same node twice to
sum up all the different ways to reach that node and write it in the answers array `answers[neighbour] = (answers[neighbour] + answers[node]) % MOD`.
If you went ahead and assigned the distances when you reach a node, like so:
    if node in distances:
        continue

    distances[node] = time

This way, you will never reach the same node twice, which you need to do in order to get the correct result here.
Testcase #3 from my questions is a GREAT example for that.
Once you reach node 3 from node 4 and write it in distances array, you will no longer consider that node from the node 2,
but it has the same time so you SHOULD BE considering that path since you need the number of ALL paths.

NOTE: Also, small detail crucial to this problem and this solution which I have written at the top of these notes but will repeat it again.
When you go with the solution of writing distances in the if statement and visiting same nodes multiple times if necessary,
you will have to nullify the value of the node in the answers array IF you find a shorted path, like so:
    if new_time < distances[neighbour]:
        heappush(heap, (new_time, neighbour))
        distances[neighbour] = new_time
        answers[neighbour] = 0

The last line is important here, thats what this note is about.
If you don't nullify it, your code will fail on my testcase #3 (I say my testcase but it was taken from leetcode 😊)
"""

from heapq import heappop, heappush
from typing import List


"""
TIME: 24ms (Beats 25.42%)
MEM: 25.18MB (Beats 41.15%)
NOTE: This is with dictionaries (graph, distances, answers)

TIME: 16ms (Beats 77.42%)
MEM: 25.00MB (Beats 82.96%)
NOTE: Now THIS is with arrays (graph, distances, answers), good shit!

NOTE: Arrays > Dictionaries
"""


class Solution(object):
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for s, e, t in roads:
            graph[s].append((e, t))
            graph[e].append((s, t))

        heap = [(0, 0)]
        distances = [float("inf")] * n
        answers = [0] * n
        answers[0] = 1
        while heap:
            time, node = heappop(heap)

            for neighbour, neighbour_time in graph[node]:
                new_time = time + neighbour_time

                if new_time < distances[neighbour]:
                    heappush(heap, (new_time, neighbour))
                    distances[neighbour] = new_time
                    answers[neighbour] = 0

                if new_time == distances[neighbour]:
                    answers[neighbour] = (answers[neighbour] + answers[node]) % MOD

        return answers[n - 1]


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            7,
            [
                [0, 6, 7],
                [0, 1, 2],
                [1, 2, 3],
                [1, 3, 3],
                [6, 3, 3],
                [3, 5, 1],
                [6, 5, 1],
                [2, 5, 1],
                [0, 4, 5],
                [4, 6, 2],
            ],
        ),
        (2, [[1, 0, 10]]),
        (
            6,
            [
                [0, 1, 5],
                [0, 2, 1],
                [1, 3, 1],
                [1, 5, 1],
                [2, 3, 2],
                [2, 4, 1],
                [3, 4, 1],
            ],
        ),
    ]

    for n, roads in q:
        print("n: ", n)
        print(*roads, sep="\n")
        print()
        answer = solution.countPaths(n, roads)
        print("answer: ", answer)
        print("=====================")
        print()
