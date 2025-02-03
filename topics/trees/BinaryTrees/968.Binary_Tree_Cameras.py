from utils import array_to_node_tree

class Solution(object):
  
  answer = 0

  def minCameraCover(self, root):
    self.answer = 0
    (_, is_root_covered) = self.traverse(root)
    
    if not is_root_covered:
      self.answer += 1
    
    return self.answer

  # traverses the tree with post-order traversal
  # and calculates the tree
  # Returns a tuple if Booleans (camera_placed, is_covered)
  def traverse(self, root):
    if root is None:
      return (False, True)

    (left_camera_placed, left_is_covered) = self.traverse(root.left)
    (right_camera_placed, right_is_covered) = self.traverse(root.right)
    
    is_root_covered = left_camera_placed or right_camera_placed
    
    if not left_is_covered or not right_is_covered:
      self.answer += 1
      return (True, True)
    
    return (False, is_root_covered)

    


if __name__ == "__main__":
  solution = Solution()
  
  # tree = [1,2,None,3,4]
  # tree = [0,0,None,0,None,0,None,None,0]
  tree = [0]

  root = array_to_node_tree(tree)

  print("tree: ", tree);
  print("\n")
  answer = solution.minCameraCover(root)
  print("\n")
  print("answer: ", answer)