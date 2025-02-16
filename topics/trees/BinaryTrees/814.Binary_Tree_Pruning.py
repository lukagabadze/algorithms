"""
Given the root of a binary tree, return the same tree where
every subtree (of the given tree) not containing a 1 has been removed.
"""

from utils import array_to_node_tree
from binary_tree_class import traverse


class Solution(object):

    """
    This method returns a boolean value.
    If the subtree includes a 1 it returns True, otherwise False
    """

    def pruneTree(self, root):
        root_result = self.traverse_and_prune(root)

        if root_result is False:
            root = None

        return root

    def traverse_and_prune(self, node):
        # Edge case
        if node is None:
            return False

        left_tree_result = self.traverse_and_prune(node.left)
        right_tree_result = self.traverse_and_prune(node.right)

        if left_tree_result is False:
            node.left = None

        if right_tree_result is False:
            node.right = None

        final_result = (
            left_tree_result or right_tree_result or node.val == 1
        )

        return final_result


if __name__ == "__main__":
    solution = Solution()

    # tree = [1, None, 0, 0, 1]
    # tree = [1, 0, 1, 0, 0, 0, 1]
    tree = [0, None, 0, 0, 0]

    root = array_to_node_tree(tree)

    print("BEFORE: ")
    traverse(root)
    print()
    answer = solution.pruneTree(root)
    print()
    print("AFTER: ")
    traverse(root)
    print()
