"""
TODO: This code has been replicated, there are two utils.py files in trees folder.
Find a way to turn this into a module
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
it might be a good idea to teach list comprehension here as a BONUS
array is given as a "level-ordered traversal" of the tree
https://stackoverflow.com/questions/71011317/confused-about-the-way-leetcode-displays-binary-trees
"""
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


"""
HUGE Thanks to BcK https://stackoverflow.com/a/65865825/15109015
"""
def print_tree(root, val="val", left="left", right="right"):
  if not root:
    return

  def display(root, val=val, left=left, right=right):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if getattr(root, right) is None and getattr(root, left) is None:
      line = '%s' % getattr(root, val)
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle

    # Only left child.
    if getattr(root, right) is None:
      lines, n, p, x = display(getattr(root, left))
      s = '%s' % getattr(root, val)
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if getattr(root, left) is None:
      lines, n, p, x = display(getattr(root, right))
      s = '%s' % getattr(root, val)
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display(getattr(root, left))
    right, m, q, y = display(getattr(root, right))
    s = '%s' % getattr(root, val)
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

  lines, *_ = display(root, val, left, right)
  print()
  for line in lines:
      print(line)
  print()