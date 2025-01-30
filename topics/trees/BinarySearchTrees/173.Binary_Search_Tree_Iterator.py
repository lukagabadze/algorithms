"""
This is a relatively easy task, just assemble the in-order traversal tree array with values
and just answer the queries in O(1) time
"""


from utils import TreeNode, array_to_node_tree

"""
TIME: 11ms
"""
class BSTIterator(object):
  
    in_order_tree = []
    ind = 0

    def __init__(self, root):
      # Initialize in-order tree array
      self.in_order_tree = []
      self.assemble_in_order_tree(root)

      # Initialize the pointer for the queries
      self.ind = 0

    def assemble_in_order_tree(self, node):
      if node is None:
        return

      self.assemble_in_order_tree(node.left)
      self.in_order_tree.append(node.val)
      self.assemble_in_order_tree(node.right)

    def next(self):
      value = self.in_order_tree[self.ind]
      self.ind += 1
      return value

    def hasNext(self):
      return self.ind < len(self.in_order_tree)


if __name__ == "__main__":
  tree = [7, 3, 15, None, None, 9, 20];
  root = array_to_node_tree(tree)

  bSTIterator = BSTIterator(root);
  bSTIterator.next();    # return 3
  bSTIterator.next();    # return 7
  bSTIterator.hasNext(); # return True
  bSTIterator.next();    # return 9
  bSTIterator.hasNext(); # return True
  bSTIterator.next();    # return 15
  bSTIterator.hasNext(); # return True
  bSTIterator.next();    # return 20
  bSTIterator.hasNext(); # return False