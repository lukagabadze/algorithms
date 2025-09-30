from typing import List


"""
TIME: 2707ms
MEMORY: 25.29MB
NOTE: Slow as shit but works
"""


class Solution:
    def triangularSum(self, nums: List[int]) -> str:
        MOD = 10
        m = len(nums)
        for new_nums_len in list(reversed(range(m)))[:-1]:
            t = 0
            for i in reversed(range(new_nums_len)):
                a = nums[-i - 2 - t]
                b = nums[-i - 1 - t]
                t += 1

                new_num = (a + b) % MOD

                nums.append(new_num)

        return nums[-1]


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 3, 4, 5]),
        ([5]),
        ([3, 4, 5]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.triangularSum(nums)
        print("answer: ", answer)
        print("=====================")
        print()
