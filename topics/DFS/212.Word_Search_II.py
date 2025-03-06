"""
NOTE: Brute force with word search 1 algorithm gives TLE
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, word: str, word_ind: int) -> bool:
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
                    results.append(dfs(x, y, word, word_ind + 1))

            board[i][j] = tmp

            if True in results:
                return True
            else:
                return False

        answers = set()
        for word in words:
            for i in range(m):
                for j in range(n):
                    if board[i][j] != word[0]:
                        continue

                    result = dfs(i, j, word, 0)
                    if result is True:
                        answers.add(word)

        return list(answers)


if __name__ == "__main__":
    solution = Solution()

    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]

    for i, row in enumerate(board):
        print(" ".join(row))
    print()
    print("words: ", words)
    print("\n")
    answer = solution.findWords(board, words)
    print("answer: ", answer)
