class Solution:
  def floodFill(self, image, sr, sc, color):
    # Base case, nothing to change
    if image[sr][sc] == color:
      return image

    queue = [(sr, sc)]
    visited = set()
    
    root_color = image[sr][sc]
    n = len(image)
    m = len(image[0])
    
    while queue:
      (i, j) = queue.pop()
      visited.add((i, j))
      
      image[i][j] = color
      
      points_of_interest = [
        (i - 1, j),
        (i + 1, j),
        (i, j + 1),
        (i, j - 1),
      ]
      filtered = [
        (i, j) for (i, j) in points_of_interest
        if (i >= 0 and j >= 0 and i < n and j < m)
        and image[i][j] == root_color
        and (i, j) not in visited
      ]
      
      queue += filtered

    return image


if __name__ == "__main__":
  solution = Solution()
  
  # image = [[1,1,1],[1,1,0],[1,0,1]]
  # sr = 1
  # sc = 1
  # color = 2

  image = [[0,0,0],[0,0,0]]
  sr = 0
  sc = 0
  color = 0

  print("image:");
  for row in image:
    print(" ".join(map(str, row)))

  print("\n")
  answer = solution.floodFill(image, sr, sc, color)
  print("answer: ")
  for row in answer:
    print(" ".join(map(str, row)))