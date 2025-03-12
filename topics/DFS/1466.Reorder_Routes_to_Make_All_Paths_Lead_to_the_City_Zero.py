from collections import deque, defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Fill the connections map in reverse mode since I want to run DFS from the node 0
        conn_map = defaultdict(list)
        conn_map_reversed = defaultdict(list)
        for [node1, node2] in connections:
            conn_map[node2].append(node1)
            conn_map_reversed[node1].append(node2)

        stack = deque([0])
        visited = set([0])
        answer = 0
        while stack:
            node = stack.pop()

            direct_nodes = conn_map[node]
            reverse_nodes = conn_map_reversed[node]

            answer += len(set(reverse_nodes) - visited)

            for node in direct_nodes + reverse_nodes:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)

        return answer


if __name__ == "__main__":
    solution = Solution()

    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

    # n = 5
    # connections = [[1, 0], [1, 2], [3, 2], [3, 4]]

    # n = 3
    # connections = [[1, 0], [2, 0]]

    print("n: ", n)
    for i, row in enumerate(connections):
        print(" ".join(map(str, row)))
    print("\n")
    answer = solution.minReorder(n, connections)
    print("answer: ", answer)
