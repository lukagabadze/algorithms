from typing import List
from collections import deque


"""
TIME: 8424ms (Beats 5.07%) Not even funny how slow this is.
But, the Memory is 19.34MB (Beats 84.28%) which is weird.
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        stack = deque([(i, j, 1) for i in range(m) for j in range(n)])
        answer = 0
        answer_map = [[1 for _ in range(n)] for _ in range(m)]
        while stack:
            (i, j, count) = stack.pop()

            answer = max(answer, count)

            points_of_interest = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]
            for x, y in points_of_interest:
                if (
                    (x >= 0 and x < m and y >= 0 and y < n)
                    and (answer_map[x][y] <= count + 1)
                    and (matrix[x][y] > matrix[i][j])
                ):
                    stack.append((x, y, count + 1))
                    answer_map[x][y] = count + 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    # matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]

    # matrix = [[1, 2]]

    print("matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

    print("\n")
    answer = solution.longestIncreasingPath(matrix)
    print("answer: ", answer)
