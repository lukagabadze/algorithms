"""
This problem does not involve graphs or trees so
I think this should be tough later just to teach that
BFS also applies with matrixes and other data types
NOTE: You can teach list comprehension here as well as a BONUS
"""

from collections import deque

class Solution(object):
  def pacificAtlantic(self, heights):
    visited = set()
    answers_map = [[(False, False)] * len(row) for row in heights]

    # for row in answers_map:
    #   print(" ".join(map(str, row)))

    m = len(heights)
    n = len(heights[0])
    
    for i in range(m):
      for j in range(n):
        if (i, j) in visited:
          continue
        
        queue = deque([(i, j, False, False)])
        # visited.add((i, j))
        visited = {(i, j)}
        while queue:
          (i, j, pacific, atlantic) = queue.popleft()
          visited.add((i, j))
          
          pacific = pacific or i == 0 or j == 0
          atlantic = atlantic or i == m - 1 or j == n - 1
          print('i, j', i, j)
          answers_map[i][j] = (pacific, atlantic)
          
          points_of_interest = [
            (i - 1, j),
            (i + 1, j),
            (i, j + 1),
            (i, j - 1),
          ]
          filtered = [
            (x, y, pacific, atlantic) for (x, y) in points_of_interest
            if (x, y) not in visited
            and x >= 0 and x < m and y >= 0 and y < n
            and heights[x][y] <= heights[i][j]
          ]
          queue.extend(filtered)

    # for row in answers_map:
    #   print(" ".join(map(str, row)))

    
    answer = []
    for i in range(m):
      for j in range(n):
        if answers_map[i][j] == (True, True):
          answer.append([i, j])

    return answer


if __name__ == "__main__":
  solution = Solution()
  
  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

  print("heights:");
  for row in heights:
    print(" ".join(map(str, row)))

  print("\n")
  answer = solution.pacificAtlantic(heights)
  print("answer: ", answer)