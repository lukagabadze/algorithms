class Solution(object):
    def maxAreaOfIsland(self, grid):
        lands = []
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == 1:
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

            queue = [(i, j)]
            visited.add((i, j))
            ans = 1
            while queue:
                (i, j) = queue.pop(0)  # Pop from left

                points_of_interest = [
                    (i, j - 1),
                    (i, j + 1),
                    (i - 1, j),
                    (i + 1, j),
                ]

                for x, y in points_of_interest:
                    if (
                        (x >= 0 and x < m and y >= 0 and y < n)
                        and (x, y) not in visited
                        and grid[x][y] == 1
                    ):
                        queue.append((x, y))
                        visited.add((x, y))
                        ans += 1

            answer = max(answer, ans)

        return answer


if __name__ == "__main__":
    solution = Solution()

    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]

    # grid = [
    #   [1, 1, 1, 1, 0],
    #   [1, 1, 0, 1, 0],
    #   [1, 1, 0, 0, 0],
    #   [0, 0, 0, 0, 0]
    # ]

    # grid = [
    #   [1, 1, 0, 0, 0],
    #   [1, 1, 0, 0, 0],
    #   [0, 0, 1, 0, 0],
    #   [0, 0, 0, 1, 1]
    # ]

    print("grid:")
    for row in grid:
        print(" ".join(map(str, row)))

    print("\n")
    answer = solution.maxAreaOfIsland(grid)
    print("answer: ", answer)
