"""
Solved using a normal way.
I also have a solution with AVL Trees which is slow as a snail
but it's good to study AVL Trees
"""

from utils import TreeNode, array_to_node_tree


class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root


if __name__ == "__main__":
    solution = Solution()

    tree = [4, 2, 7, 1, 3]
    val = 5

    root = array_to_node_tree(tree)

    print("tree: ", tree)
    print("val: ", val)
    print("\n")
    new_root = solution.insertIntoBST(root, val)

    def print_in_order(root):
        if root is None:
            return

        print_in_order(root.left)
        print(root.val, end=" ")
        print_in_order(root.right)
        return

    print_in_order(new_root)
