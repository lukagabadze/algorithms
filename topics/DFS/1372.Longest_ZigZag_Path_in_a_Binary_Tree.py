"""
NOTE: DFS was the correct choice for this problem, but why can't BFS work?
TODO: See what happens when you use BFS on this problem.

NOTE: I changed the stack to a queue and the result is 3ms faster, now this was only run once so the results are rough estimates,
so I am concluding that both BFS and DFS perform the same here, they are both O(n) algorithms in this case.
I am committing this BFS solution but I will commit a DFS solution after it so that my DFS folder holds DFS solutions.
"""

from utils import array_to_node_tree, print_tree
from collections import deque


"""
DFS TIME: 61ms (Beats 63.67%)
I am BLAZING through these problems!

BFS TIME 59ms (Beats 70.42%)
I thought I finally found a good DFS problem but in this problem it does not matter if you use BFS or DFS, they have the same result...
"""


class Solution(object):
    def longestZigZag(self, root):
        queue = deque([(root, None, 0)])
        visited = set([root])
        answer = 0
        while queue:
            (node, direction, depth) = queue.popleft()

            answer = max(answer, depth)

            if node.right and node.right not in visited:
                new_depth = depth + 1
                if direction == "R":
                    new_depth = 1
                queue.append((node.right, "R", new_depth))
                visited.add(node.right)

            if node.left and node.left not in visited:
                new_depth = depth + 1
                if direction == "L":
                    new_depth = 1
                queue.append((node.left, "L", new_depth))
                visited.add(node.left)

        return answer


if __name__ == "__main__":
    solution = Solution()

    # tree = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]

    tree = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]

    root = array_to_node_tree(tree)
    print_tree(root)
    print("\n")
    answer = solution.longestZigZag(root)
    print("answer: ", answer)
