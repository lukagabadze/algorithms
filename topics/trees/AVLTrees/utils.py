class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_node_tree(arr):
  nodes = [TreeNode(val) if val is not None else None for val in arr]

  n = len(nodes)
  j = 0

  for i in range(n):
    if nodes[i] is not None:
      
      left = j + 1
      right = j + 2
      j += 2

      if left < n:
        nodes[i].left = nodes[left]      
      
      if right < n:
        nodes[i].right = nodes[right]      

  # Return the root of the tree
  return nodes[0]