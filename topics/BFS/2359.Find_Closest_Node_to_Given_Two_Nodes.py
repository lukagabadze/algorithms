from typing import List
from collections import deque


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        visited_1 = [-1] * n
        visited_2 = [-1] * n
        queue = deque([(node1, 0, 1), (node2, 0, 2)])

        while queue:
            node, depth, node_type = queue.popleft()

            if node_type == 1:
                visited_1[node] = depth

                neighbour = edges[node]
                if visited_1[neighbour] == -1 and neighbour != -1:
                    queue.append((neighbour, depth + 1, 1))

            if node_type == 2:
                visited_2[node] = depth

                neighbour = edges[node]
                if visited_2[neighbour] == -1 and neighbour != -1:
                    queue.append((neighbour, depth + 1, 2))

        answer = -1
        max_dist = float("inf")
        for i in range(n):
            if visited_1[i] == -1 or visited_2[i] == -1:
                continue

            i_max = max(visited_1[i], visited_2[i])
            if i_max < max_dist:
                answer = i
                max_dist = i_max

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([2, 2, 3, -1], 0, 1),
        ([1, 2, -1], 0, 2),
        ([5, 4, 5, 4, 3, 6, -1], 0, 1),
        ([4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6),
        ([3, 0, 5, -1, 3, 4], 2, 0),
    ]

    for edges, node1, node2 in q:
        print("edges: ", edges)
        print("node1: ", node1)
        print("node2: ", node2)
        print()
        answer = solution.closestMeetingNode(edges, node1, node2)
        print("answer: ", answer)
        print("=====================")
        print()
