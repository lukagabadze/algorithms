from typing import List


"""
Initial Time: 5367ms (Beats 24.04%)
I can do better!

Second Attempt Time: 3669ms (Beats 70.61%)
Huge thanks to the GOAT firdavs for the solution (https://leetcode.com/problems/word-search/solutions/4965052/96-45-easy-solution-with-explanation)

NOTE: Looks like recursive dfs performs way better here than the stack dfs.
This might be due to having a visited set in each step of the stack,
while here, you just unassign the point and assign it back after checking all neighbours.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, word_ind: int) -> bool:
            if word_ind == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = ""

            points_of_interest = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]
            results = []
            for x, y in points_of_interest:
                if (
                    x >= 0
                    and y >= 0
                    and x < m
                    and y < n
                    and board[x][y] == word[word_ind + 1]
                ):
                    results.append(dfs(x, y, word_ind + 1))

            board[i][j] = tmp

            if True in results:
                return True
            else:
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue

                result = dfs(i, j, 0)
                if result is True:
                    return True

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
