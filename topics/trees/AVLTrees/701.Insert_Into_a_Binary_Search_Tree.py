
from utils import TreeNode, array_to_node_tree, print_tree


class AVLTreeNode(object):
    def __init__(self, val=0, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height


"""
NOTE: This problem does not require AVL Trees, but in order to learn
about AVL Trees, I am going to solve it using left/right rotations.

TIME: 620ms
SLOW AS SHIT
but it's AVL Trees so good to learn
"""


class Solution(object):

    def insertIntoBST(self, root, val):
        def navigate(root):
            if root is None:
                return []
            left = navigate(root.left)
            right = navigate(root.right)
            return left + right + [root.val]

        nodes = navigate(root) + [val]

        root = None
        for node in nodes:
            root = self.insert(root, node)

        # Convert it back to BSF TreeNode
        def convert(root):
            if root:
                return TreeNode(root.val, convert(root.left), convert(root.right))

        return convert(root)

    def insert(self, root, val):
        if root is None:
            return AVLTreeNode(val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)

        # Update the height after insert
        self.set_height(root)

        # After inserting, let's balance the tree
        # Balancing it takes O(1) time

        # Balance Factor
        bf = self.get_height(root.left) - self.get_height(root.right)

        # Right heavy, do left rotation
        if bf < -1 and val > root.right.val:
            return self.left_rotate(root)

        # Left heavy, do right rotation
        if bf > 1 and val < root.left.val:
            return self.right_rotate(root)

        # Left Right heavy, do left and then right rotation
        if bf > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if bf < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # If none of the above if statements are true,
        # that means the subtree is balanced, return root
        return root

    def left_rotate(self, node):
        A = node
        B = node.right
        temp = B.left

        B.left = A
        A.right = temp

        self.set_height(A)
        self.set_height(B)

        return B

    def right_rotate(self, node):
        A = node
        B = node.left
        temp = B.right

        B.right = A
        A.left = temp

        self.set_height(A)
        self.set_height(B)

        return B

    def get_height(self, node):
        return 0 if not node else node.height

    def set_height(self, node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))


if __name__ == "__main__":
    solution = Solution()

    tree = [4, 2, 7, 1, 3]
    val = 5

    # tree = []
    # val = 5

    root = array_to_node_tree(tree)

    print_tree(root)
    print("val: ", val)
    print("\n")
    new_root = solution.insertIntoBST(root, val)
    print("ANSWER: ")
    print_tree(new_root)
