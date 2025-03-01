"""
NOTE: DFS was the correct choice for this problem, but why can't BFS work?
TODO: See what happens when you use BFS on this problem.
"""

from utils import array_to_node_tree, print_tree
from collections import deque


"""
TIME: 61ms (Beats 63.67%)
I am BLAZING through these problems!
"""


class Solution(object):
    def longestZigZag(self, root):
        stack = deque([(root, None, 0)])
        visited = set([root])
        answer = 0
        while stack:
            (node, direction, depth) = stack.pop()

            answer = max(answer, depth)

            if node.right and node.right not in visited:
                new_depth = depth + 1
                if direction == "R":
                    new_depth = 1
                stack.append((node.right, "R", new_depth))
                visited.add(node.right)

            if node.left and node.left not in visited:
                new_depth = depth + 1
                if direction == "L":
                    new_depth = 1
                stack.append((node.left, "L", new_depth))
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
