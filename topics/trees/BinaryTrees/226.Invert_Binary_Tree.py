"""
Given the root of a binary tree, invert the tree, and return its root.
"""

from utils import array_to_node_tree
from binary_tree_class import traverse


class Solution(object):

    def invertTree(self, root):
        if root is None:
            return root

        # Otherwise, the node has childer, so let's recursively swap them
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Now let's swap these two nodes if they both exist
        root.left, root.right = root.right, root.left

        return root


if __name__ == "__main__":
    solution = Solution()

    tree = [1, 2]
    # tree = [4,2,7,1,3,6,9]
    # tree = [1, 2, 3, None, 5]
    # tree = [3, 9, 20, None, None, 15, 7];
    # tree = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]

    root = array_to_node_tree(tree)

    print("BEFORE: ")
    traverse(root)
    print()
    answer = solution.invertTree(root)
    print()
    print("AFTER: ")
    traverse(root)
    print()
