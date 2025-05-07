from typing import List


class Solution(object):
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        parent = list(range(n))
        rank = [0] * n

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
                return parent[node]
            return node

        def union(a: int, b: int) -> int:
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return -1

            if rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
                return a_root
            elif rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
                return b_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1
                return a_root

        criticals = []
        visited = set()
        for i, [a, b] in enumerate(connections):
            # If one of the nodes is fresh, it might be a critical node
            # union them and save the edge as a POTENTIAL critical.
            if a not in visited or b not in visited:
                criticals.append([a, b])
                union(a, b)
                visited.add(a)
                visited.add(b)
                continue

            # We occured a loop.
            # There might be some edges we considered as critical in this loop.
            # Find and exterminate them.
            if a in visited and b in visited:
                root = find(a)
                criticals = [
                    [x, y]
                    for (x, y) in criticals
                    if find(x) != root and find(y) != root
                ]

        return criticals


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4, [[0, 1], [1, 2], [2, 0], [1, 3]]),
        (2, [[0, 1]]),
        (13, [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [4, 7], [7, 6], [6, 5], [5, 4]]),
    ]

    for n, connections in q:
        print("n: ", n)
        for a, b in connections:
            print(a, b)
        print()
        answer = solution.criticalConnections(n, connections)
        print("answer: ", answer)
        print("=====================")
        print()
