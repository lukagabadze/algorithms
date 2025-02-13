from collections import deque

"""
TIME: 688ms HORRIBLE, but accepted
TODO: Look for a better solution
"""
class Solution(object):
  def pacificAtlantic(self, heights):
    m = len(heights)
    n = len(heights[0])
    answers = []

    # Initialize the ocean map with (-1, -1).
    # This will hold the (pacific, atlantic) values for
    # every point which we already know the answer to.
    ocean_map = [[(-1, -1)] * len(row) for row in heights]
    
    for i in range(m):
      for j in range(n):

        queue = deque([(i, j)])
        visited = {(i, j)}
        pacific = False
        atlantic = False
        while queue:
          (x, y) = queue.popleft()
          
          pacific = pacific or x == 0 or y == 0
          atlantic = atlantic or x == m - 1 or y == n - 1
          
          if pacific and atlantic:
            break
          
          points_of_interest = [
            (x - 1, y),
            (x + 1, y),
            (x, y + 1),
            (x, y - 1),
          ]
          filtered = [
            (k, f) for (k, f) in points_of_interest
            if (k, f) not in visited
            and k >= 0 and k < m and f >= 0 and f < n
            and heights[k][f] <= heights[x][y]
          ]

          for k, f in filtered:
            visited.add((k, f))

            if ocean_map[k][f][0] != -1:
              pacific = pacific or ocean_map[k][f][0]
              atlantic = atlantic or ocean_map[k][f][1]
            else:
              queue.append((k, f))

        # If the point reached to both pacific and atlantic update the answers array
        if pacific and atlantic:
          answers.append([i, j])

        # Mark the result in ocean_map for later navigation
        ocean_map[i][j] = (pacific, atlantic)

    return answers


if __name__ == "__main__":
  solution = Solution()
  
  # heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  
  heights = [[2,1],[1,2]]

  print("heights:");
  for row in heights:
    print(" ".join(map(str, row)))

  print("\n")
  answer = solution.pacificAtlantic(heights)
  print("answer: ", answer)