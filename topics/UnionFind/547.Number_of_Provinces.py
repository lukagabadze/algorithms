from typing import List


"""
TIME: 8ms (Beats 38.05%)
MEMORY: 19.14MB (Beats 42.20%)

TIME: 6ms (Beats 61.77%)
MEMORY: 18.87MB (Beats 83.61%)
NOTE: I changed the final line of the code where I counted all unique root nodes:
        return len(set([find(i) for i in parent]))

But now, I just check for nodes who are their own parents, indicating that they are the root nodes:
        return sum(1 for i, val in enumerate(parent) if i == val)

TIME: 4ms (Beats 73.88%)
MEMORY: 18.83MB (Beats 83.61%)
NOTE: I added another optimization to Union Find, it's called "Path Compression".
Basically, everytime you have to find the root of the node, you can assign that root to every nodes parent as you move upwards toward that root node.
The main change is in the find method, it used to look like this:
        def find(node: int):
            while parent[node] != node:
                node = parent[node]
            return node

First unusual thing is that I use a while loop to go upwards the tree to the root node,
but the usual method is to just use recursion instead of the while loop. But it does not have any performance implications.
What DOES have impact on performance is something called "Path Compression", the code looks like this:

        def find(node: int):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

Basically, as you move upwards the tree, all the nodes you went through to reach the root node,
you update all those nodes parents (`parent[node]`) with the root nodes value.
This makes the O(logn) time complexity of the find method slowly turn into O(1).

NOTE: There was also a very small optimization inside the nested for loop where I only go through the second half of the matrix since it's mirrored.
But the main performance booster was the path compression.
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        parent = list(range(n))
        rank = [0] * n

        def find(node: int):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a: int, b: int):
            a_root = find(a)
            b_root = find(b)

            if a_root == b_root:
                return

            if rank[a_root] > rank[b_root]:
                parent[b_root] = a_root
            elif rank[a_root] < rank[b_root]:
                parent[a_root] = b_root
            else:
                parent[b_root] = a_root
                rank[a_root] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if i != j and isConnected[i][j] == 1:
                    union(i, j)

        return sum(1 for i, val in enumerate(parent) if i == val)


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]]),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ]

    for isConnected in q:
        for row in isConnected:
            print(row)
        print()
        answer = solution.findCircleNum(isConnected)
        print("answer: ", answer)
        print("=====================")
        print()
