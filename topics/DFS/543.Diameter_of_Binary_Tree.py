"""
NOTE: This is an iterative DFS solution.
MUCH MUCH MUCH better way to solve this would be by using recursive DFS which I've done many many times while learning binary trees.
So I solved this one a bit differently to learn DFS.
I admit, I got help from ChatGPT.

NOTE: Two nodes can have the same value in this problem, so the keys in `visited` set and `heights` dictionary should be `node` not `node.val`

NOTE: If you say `defaultdict(int)` it returns 0 as a default value for unassigned key.
"""

from utils import array_to_node_tree, print_tree
from collections import deque, defaultdict


class Solution(object):
    def diameterOfBinaryTree(self, root):
        answer = 0
        stack = deque([root])
        visited = set()
        heights = defaultdict(int)
        while stack:
            node = stack[-1]

            if node in visited:
                stack.pop()

                left_height = heights[node.left]
                right_height = heights[node.right]

                heights[node] = max(left_height, right_height) + 1

                answer = max(answer, left_height + right_height)

            if node not in visited:
                visited.add(node)

                # Child Nodes
                cnodes = [node.right, node.left]
                for cnode in cnodes:
                    if cnode is not None:
                        stack.append(cnode)

        return answer


if __name__ == "__main__":
    solution = Solution()

    tree = [1, 2, 3, 4, 5]

    # tree = [1, 2]

    root = array_to_node_tree(tree)
    print_tree(root)
    print("\n")
    answer = solution.diameterOfBinaryTree(root)
    print("answer: ", answer)
