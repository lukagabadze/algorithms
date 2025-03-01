"""
NOTE: Super interesting and weird:
If you say `max(max(answer_map))` it returns a wrong result, to get the correct result you should write `max(max(row) for row in answer_map)`
WHY? 😭😭😭
"""

from typing import List


"""
INITIAL TIME: 8424ms (Beats 5.07%) Not even funny how slow this is.
But, the Memory is 19.34MB (Beats 84.28%) which is weird.

NEW TIME: 128ms (Beats 85.88%) Fuck Yeah I am the GOAT!!!!!!!
Memory: 19.86MB (Beats 62.36%)
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        answer_map = [[None for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            depth = 1

            if answer_map[i][j]:
                return answer_map[i][j]

            points_of_interest = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]
            for x, y in points_of_interest:
                if (x >= 0 and x < m and y >= 0 and y < n) and (
                    matrix[x][y] > matrix[i][j]
                ):
                    depth = max(depth, dfs(x, y) + 1)

            answer_map[i][j] = depth
            return depth

        for i, j in [(i, j) for i in range(m) for j in range(n)]:
            dfs(i, j)

        return max(max(row) for row in answer_map)


if __name__ == "__main__":
    solution = Solution()

    # matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    # matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]

    # matrix = [[1, 2]]

    matrix = [[7, 7, 5], [2, 4, 6], [8, 2, 0]]

    print("matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

    print("\n")
    answer = solution.longestIncreasingPath(matrix)
    print("answer: ", answer)
