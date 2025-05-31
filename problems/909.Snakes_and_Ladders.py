from typing import List


class Solution(object):
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        INF = float("inf")
        n = len(board)

        def num_to_inds(num: int) -> [int, int]:
            i = n - ((num - 1) // n) - 1
            j = 0

            if (n - i) % 2 == 0:
                j = n - ((num - 1) % n) - 1
            else:
                j = (num - 1) % n

            return [i, j]

        def inds_to_num(i: int, j: int) -> int:
            num = (n - i) * n

            if (n - i) % 2 == 0:
                num -= j
            else:
                num += j - n + 1

            return num

        answers = [[INF] * n for _ in range(n)]
        answers[n - 1][0] = 0

        for i in reversed(range(n)):
            for j in range(n):
                num = inds_to_num(i, j)

                # Dice
                for k in range(1, 7):
                    x, y = num_to_inds(num + k)

                    if num + k > n * n:
                        continue

                    if board[x][y] != -1:
                        tmp_i, tmp_j = num_to_inds(board[x][y])
                        answers[tmp_i][tmp_j] = min(
                            answers[tmp_i][tmp_j], answers[i][j] + 1
                        )
                    else:
                        answers[x][y] = min(answers[x][y], answers[i][j] + 1)

        i, j = num_to_inds(n * n)
        return answers[i][j] if answers[i][j] != INF else -1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ]
        ),
        ([[-1, -1], [-1, 3]]),
        ([[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]),
        ([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]),
    ]

    for board in q:
        print("board:")
        for row in board:
            print(row)
        print()
        answer = solution.snakesAndLadders(board)
        print("answer: ", answer)
        print("=====================")
        print()
