"""
This problem does not involve graphs or trees so
I think this should be tough later just to teach that
BFS also applies with matrixes and other data types
NOTE: You can teach list comprehension here as well as a BONUS
"""


class Solution(object):
    def numIslands(self, grid):
        lands = []
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == "1":
                    lands.append((i, j))

        if not lands:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = set()
        answer = 0

        for i, j in lands:
            if (i, j) in visited:
                continue

            answer += 1
            queue = [(i, j)]
            while queue:
                (x, y) = queue.pop(0)  # Pop from left

                # Two ways of doing the checks
                # 1) array and list comprehension
                # 2) four if statements (easier for beginners)

                # # First method
                # points_of_interest = [
                #   (x, y - 1),
                #   (x, y + 1),
                #   (x - 1, y),
                #   (x + 1, y),
                # ]

                # for x, y in points_of_interest:
                #   if (
                #     ((x, y) not in visited) and  # it is not visited
                #     (x >= 0 and x < m and y >= 0 and y < n) and # it is in range of grid width and length
                #     (grid[x][y] == '1')  # it is a land
                #   ):
                #     queue.append((x, y))
                #     visited.add((x, y))

                # Second method
                if x - 1 >= 0 and grid[x - 1][y] == "1" and (x - 1, y) not in visited:
                    queue += [(x - 1, y)]
                    visited.add((x - 1, y))

                if x + 1 < m and grid[x + 1][y] == "1" and (x + 1, y) not in visited:
                    queue += [(x + 1, y)]
                    visited.add((x + 1, y))

                if y - 1 >= 0 and grid[x][y - 1] == "1" and (x, y - 1) not in visited:
                    queue += [(x, y - 1)]
                    visited.add((x, y - 1))

                if y + 1 < n and grid[x][y + 1] == "1" and (x, y + 1) not in visited:
                    queue += [(x, y + 1)]
                    visited.add((x, y + 1))

        return answer


if __name__ == "__main__":
    solution = Solution()

    # grid = [
    #   ["1","1","1","1","0"],
    #   ["1","1","0","1","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","0","0","0"]
    # ]

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    print("grid:")
    for row in grid:
        print(" ".join(row))

    print("\n")
    answer = solution.numIslands(grid)
    print("answer: ", answer)
