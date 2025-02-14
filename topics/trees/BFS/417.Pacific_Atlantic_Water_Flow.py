"""
Thanks to the GOAT Abhishek for the amazing solution!
https://leetcode.com/problems/pacific-atlantic-water-flow/solutions/1126938/short-easy-w-explanation-diagrams-simple-graph-traversals-dfs-bfs/
"""


from collections import deque

"""
TIME: 65ms
NOTE: Much better than my previous brute force BFS solution.
"""
class Solution(object):
  def pacificAtlantic(self, heights):
    m = len(heights)
    n = len(heights[0])
    
    def travel(queue):
      visited = set()
      while queue:
        (x, y) = queue.popleft()
        visited.add((x, y))
        
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
          and heights[k][f] >= heights[x][y]
        ]

        for k, f in filtered:
          queue.append((k, f))
      return visited

    # Pacific edges (range(1, n) to avoid putting (0, 0) twice)
    queue = deque([(i, 0) for i in range(m)] + [(0, i) for i in range(1, n)])
    pacific_visited = travel(queue)
    
    # Atlantic edges (range(n-1) to avoid putting (m, n) twice)
    queue = deque([(i, n - 1) for i in range(m)] + [(m - 1, i) for i in range(n - 1)])
    atlantic_visited = travel(queue)
    
    # Answers are points which were covered in poth pacific and atlantic BFS travels
    answers = [[i, j] for i, j in pacific_visited & atlantic_visited]

    return answers


if __name__ == "__main__":
  solution = Solution()
  
  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  
  # heights = [[2,1],[1,2]]

  print("heights:");
  for row in heights:
    print(" ".join(map(str, row)))

  print("\n")
  answer = solution.pacificAtlantic(heights)
  print("answer: ", answer)