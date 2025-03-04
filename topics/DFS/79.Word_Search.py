from collections import deque
from typing import List


"""
Initial Time: 5367ms (Beats 24.04%)
I can do better!
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for initial_i in range(m):
            for initial_j in range(n):
                if board[initial_i][initial_j] != word[0]:
                    continue

                stack = deque(
                    [(initial_i, initial_j, 0, set([(initial_i, initial_j)]))]
                )
                while stack:
                    (i, j, word_ind, visited) = stack.pop()

                    if word_ind == len(word) - 1:
                        return True

                    points_of_interest = [
                        (i + 1, j),
                        (i - 1, j),
                        (i, j + 1),
                        (i, j - 1),
                    ]
                    for x, y in points_of_interest:
                        if (
                            (x >= 0 and y >= 0 and x < m and y < n)
                            and ((x, y) not in visited)
                            and (board[x][y] == word[word_ind + 1])
                        ):
                            new_visited = visited.copy()
                            new_visited.add((x, y))

                            stack.append((x, y, word_ind + 1, new_visited))

        return False


if __name__ == "__main__":
    solution = Solution()

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "SEE"

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"

    # board = [["a", "a"]]
    # word = "aaa"

    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"

    for i, row in enumerate(board):
        print(" ".join(row))
    print()
    print("word: ", word)
    print("\n")
    answer = solution.exist(board, word)
    print("answer: ", answer)
