from typing import List


"""
TIME: 7ms (Beats 23.71%)
NOTE: This is without checking if need to run the row/column for loop.
"""


class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue

                # Column loop
                for k in range(m):
                    if matrix[k][j] != 0:
                        matrix[k][j] = None

                # Row loop
                for k in range(n):
                    if matrix[i][k] != 0:
                        matrix[i][k] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]),
        ([[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]),
    ]

    for matrix in q:
        print("matrix: ", matrix)
        print()
        solution.setZeroes(matrix)
        print("answer: ", matrix)
        print("=====================")
        print()
