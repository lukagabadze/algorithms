class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        # Base case
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = [(0, 0, 1)]
        visited = set()

        answer = -1
        while queue:
            (i, j, ans) = queue.pop(0)  # Pop from front

            if i == n - 1 and j == n - 1:
                answer = ans
                break

            points_of_interest = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
                (i - 1, j - 1),
                (i + 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j + 1),
            ]

            for x, y in points_of_interest:
                if (
                    (x >= 0 and y >= 0 and x < n and y < n)
                    and (x, y) not in visited
                    and grid[x][y] == 0
                ):
                    queue.append((x, y, ans + 1))
                    visited.add((x, y))

        return answer


if __name__ == "__main__":
    solution = Solution()

    # grid = [
    #   [0,1],
    #   [1,0],
    # ]

    grid = [
        [0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    # grid = [
    #   [0,0,0],
    #   [1,1,0],
    #   [1,1,0],
    # ]

    # grid = [
    #   [0,0,0],
    #   [0,1,0],
    #   [0,0,0],
    # ]

    print("grid:")
    for row in grid:
        print(" ".join(map(str, row)))

    print("\n")
    answer = solution.shortestPathBinaryMatrix(grid)
    print("answer: ", answer)
