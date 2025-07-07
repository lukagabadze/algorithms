from typing import List


class Solution(object):
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2

            days_took = 1
            curr_w = 0
            for w in weights:
                if curr_w + w > mid:
                    curr_w = 0
                    days_took += 1

                curr_w += w

            if days_took > days:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([3, 2, 2, 4, 1, 4], 3),
        ([1, 2, 3, 1, 1], 4),
    ]

    for weights, days in q:
        print("weights: ", weights)
        print("days: ", days)
        print()
        answer = solution.shipWithinDays(weights, days)
        print("answer: ", answer)
        print("=====================")
        print()
