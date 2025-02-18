from collections import deque
from typing import List


"""
TIME: 3ms (Beats 97.08%) HELL YEAH!
I AM THE GOAT!
"""


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        source = "".join(map(str, [val for row in board for val in row]))
        target = "123450"

        if source == target:
            return 0

        queue = deque([(source, 0)])
        visited = set(source)
        while queue:
            (state, ans) = queue.popleft()
            possible_states = self.get_possible_states(state)

            for pos_state in possible_states:
                if pos_state not in visited:
                    queue.append((pos_state, ans + 1))
                    visited.add(pos_state)

                    if pos_state == target:
                        return ans + 1

        return -1

    def get_possible_states(self, state):
        arr = list(state)
        possible_states = []

        if arr[5] == "0":
            possible_states.append(f"{arr[0]}{arr[1]}{arr[5]}{arr[3]}{arr[4]}{arr[2]}")
            possible_states.append(f"{arr[0]}{arr[1]}{arr[2]}{arr[3]}{arr[5]}{arr[4]}")

        if arr[4] == "0":
            possible_states.append(f"{arr[0]}{arr[4]}{arr[2]}{arr[3]}{arr[1]}{arr[5]}")
            possible_states.append(f"{arr[0]}{arr[1]}{arr[2]}{arr[4]}{arr[3]}{arr[5]}")
            possible_states.append(f"{arr[0]}{arr[1]}{arr[2]}{arr[3]}{arr[5]}{arr[4]}")

        if arr[3] == "0":
            possible_states.append(f"{arr[3]}{arr[1]}{arr[2]}{arr[0]}{arr[4]}{arr[5]}")
            possible_states.append(f"{arr[0]}{arr[1]}{arr[2]}{arr[4]}{arr[3]}{arr[5]}")

        if arr[2] == "0":
            possible_states.append(f"{arr[0]}{arr[2]}{arr[1]}{arr[3]}{arr[4]}{arr[5]}")
            possible_states.append(f"{arr[0]}{arr[1]}{arr[5]}{arr[3]}{arr[4]}{arr[2]}")

        if arr[1] == "0":
            possible_states.append(f"{arr[0]}{arr[4]}{arr[2]}{arr[3]}{arr[1]}{arr[5]}")
            possible_states.append(f"{arr[1]}{arr[0]}{arr[2]}{arr[3]}{arr[4]}{arr[5]}")
            possible_states.append(f"{arr[0]}{arr[2]}{arr[1]}{arr[3]}{arr[4]}{arr[5]}")

        if arr[0] == "0":
            possible_states.append(f"{arr[1]}{arr[0]}{arr[2]}{arr[3]}{arr[4]}{arr[5]}")
            possible_states.append(f"{arr[3]}{arr[1]}{arr[2]}{arr[0]}{arr[4]}{arr[5]}")

        return possible_states


if __name__ == "__main__":
    solution = Solution()

    # board = [[1, 2, 3], [4, 0, 5]]

    # board = [[1, 2, 3], [5, 4, 0]]

    board = [[4, 1, 2], [5, 0, 3]]

    for row in board:
        print(" ".join(map(str, row)))
    print("\n")
    answer = solution.slidingPuzzle(board)
    print("answer: ", answer)
