from typing import List
from collections import deque


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        answer = 0
        queue = deque(initialBoxes)
        visited = set()
        needs_keys = set()
        while queue:
            box = queue.popleft()

            # If this box has been processed, continue
            if box in visited:
                continue

            # If this box is NOT open, continue
            if status[box] == 0:
                needs_keys.add(box)
                continue

            answer += candies[box]
            visited.add(box)

            for key in keys[box]:
                status[key] = 1
                if key in needs_keys and key not in visited:
                    queue.append(key)

            for containedBox in containedBoxes[box]:
                if containedBox not in visited:
                    queue.append(containedBox)

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]),
        (
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [[1, 2, 3, 4, 5], [], [], [], [], []],
            [0],
        ),
    ]

    for status, candies, keys, containedBoxes, initialBoxes in q:
        print("status: ", status)
        print("candies: ", candies)
        print("keys: ", keys)
        print("containedBoxes: ", containedBoxes)
        print("initialBoxes: ", initialBoxes)
        print()
        answer = solution.maxCandies(
            status, candies, keys, containedBoxes, initialBoxes
        )
        print("answer: ", answer)
        print("=====================")
        print()
