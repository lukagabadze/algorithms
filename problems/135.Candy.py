from typing import List
from collections import deque


class Solution(object):
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        order = sorted([(rating, i) for i, rating in enumerate(ratings)])

        queue = deque([ind for [_, ind] in order])
        visited = [False] * n
        answers = [0] * n
        while queue:
            ind = queue.popleft()

            if visited[ind]:
                continue

            visited[ind] = True

            # Check left
            if ind > 0 and not visited[ind - 1] and ratings[ind - 1] > ratings[ind]:
                answers[ind - 1] = answers[ind] + 1
                queue.append(ind - 1)

            # Check right
            if ind < n - 1 and not visited[ind + 1] and ratings[ind + 1] > ratings[ind]:
                answers[ind + 1] = answers[ind] + 1
                queue.append(ind + 1)

        return sum(answers) + n


if __name__ == "__main__":
    solution = Solution()

    q = [([1, 0, 2]), ([1, 2, 2]), ([7, 6, 9, 3, 4, 6, 10]), ([0, 1, 2, 3, 2, 1])]

    for ratings in q:
        print("ratings: ", ratings)
        print()
        answer = solution.candy(ratings)
        print("answer: ", answer)
        print("=====================")
        print()
