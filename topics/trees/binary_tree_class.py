"""
There are 2 ways to store a binary tree

1) Using a class (called Linked Representation)
2) Using an array


This file is gonna show the class implementation
"""


class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def traverse(node):
  if node is not None:
    print(node.val, end=" ")
    traverse(node.left)
    traverse(node.right)


if __name__ == "__main__":
  root = TreeNode(10)
  root.left = TreeNode(3)
  root.right = TreeNode(5)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(9)
  root.right.left = TreeNode(11)
  root.right.right = TreeNode(23)

  traverse(root)