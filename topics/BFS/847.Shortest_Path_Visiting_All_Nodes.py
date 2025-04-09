"""

NOTE: I am getting time limit exceeded errors, I am NOT the GOAT today...
But I have an idea which might cut out some nodes I have to visit:
There are three reasons why we should check out the next node (append to the queue)
1) The path has not been visited yet `(node, next_node) not in visited_paths`
2) The node has not been visited yet `next_node not in visited_nodes`
3) The node has other unvisited nodes to offer us `len(set(graph[next_node]) - visited_nodes) > 0`

NOTE: This was my last desperate attempt at solving this problem.
I followed the instructions above, but instead of just looking at what a node had to offer,
I had to keep track of nodes I did not take and put them into possible_nodes.
This gets the right answer but it's still slow as SHIT, time limit exceeded :(

NOTE: Little intuition
going from each node one by one, is kinda like DFS, when this solution requires BFS.
It would be better to fill the queue with initial notes first and the virst one to visit all nodes wins.
Thank you to the GOAT Panda for the solution: https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/135809/fast-bfs-solution-46ms-clear-detailed-explanation-included/
Glad I understand this problem now.

NOTE: My way of solving was correct but had 2 major problems:
1) I had a for loop where I ran BFS from every node only when the last node was finished.
This was a major flaw since it was no longer BFS, I had to calculate the answer using `answer = min(answer, ans)`.
This has been fixed now by filling the queue with each node as a starter node before starting the BFS while loop.
This ensures that the first time you visit all nodes, it is the shortest path!!!

2) Second major mistake was my way of keeping track of visited_nodes.
I had a set of nodes, which I used to transform into a string like this `1-3-6-7-9`,
I also had to sort it which added more time, time which was very crucial to this problem.
This has been fixed by Bitmasks, holy fucking shit bitmasks are cool.
Bitmasks took my solution into another level in terms of performance.
Cool skill to have!
Bit Masking Tutorial: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/
"""

from collections import deque
from typing import List


"""
TIME: 111ms (Beats 89.36%)
Bitmasks are BLAZING FAST WTF?!
"""


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph[0]:
            return 0

        # Number of nodes
        n = len(graph)
        target = (1 << n) - 1

        answer = float("+inf")
        visited = set()
        queue = deque()

        # Fill the queue with every node as a started node.
        # This ensures that the first time we visit all nodes, it will be the shortest!
        for i in range(len(graph)):
            queue.append((i, 1 << i, 0))
            visited.add((i, 1 << i))

        while queue:
            (node, visited_nodes_mask, ans) = queue.popleft()

            if visited_nodes_mask == target:
                answer = min(answer, ans)
                break

            for next_node in graph[node]:
                # Calculate the next_node_visited_mask using the
                # visited_nodes_mask with the XOR operation on a
                # bitmask with only next_node set as 1 (1 << next_node)
                next_node_visited_mask = visited_nodes_mask | (1 << next_node)

                if (next_node, next_node_visited_mask) not in visited:
                    # Found the answer, since it's BFS, return, it's the shortest
                    if next_node_visited_mask == target:
                        return ans + 1

                    queue.append((next_node, next_node_visited_mask, ans + 1))
                    visited.add((next_node, next_node_visited_mask))

        return -1


if __name__ == "__main__":
    solution = Solution()

    # graph = [[1, 2, 3], [0], [0], [0]]

    # graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]

    graph = [
        [2, 10],
        [2, 7],
        [0, 1, 3, 4, 5, 8],
        [2],
        [2],
        [2],
        [8],
        [9, 11, 8, 1],
        [7, 6, 2],
        [7],
        [11, 0],
        [7, 10],
    ]

    # graph = [[2, 3], [7], [0, 6], [0, 4, 7], [3, 8], [7], [2], [5, 3, 1], [4]]

    # graph = [[1], [0, 2, 4], [1, 3], [2], [1, 5], [4]]

    for i, row in enumerate(graph):
        print(i, end=": ")
        print(" ".join(map(str, row)))
    print("\n")
    answer = solution.shortestPathLength(graph)
    print("answer: ", answer)
