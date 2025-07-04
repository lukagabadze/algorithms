from typing import List


class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l_left, l_right, l_ans = 0, n - 1, 0
        r_left, r_right, r_ans = 0, n - 1, 0

        while l_left < l_right or r_left < r_right:
            l_mid = (l_left + l_right) // 2
            r_mid = (r_left + r_right) // 2

            print("r_left: ", r_left)
            print("r_right: ", r_right)
            print("r_mid: ", r_mid)
            print("nums[r_mid]: ", nums[r_mid])

            if l_mid < n - 1:
                if nums[l_mid] < nums[l_mid + 1]:
                    l_right = l_mid
                else:
                    l_ans = l_mid + 1
                    l_left = l_mid + 1

            if r_mid < n - 1:
                if nums[r_mid] < nums[r_mid + 1]:
                    r_left = r_mid + 1
                else:
                    r_ans = r_mid + 1
                    r_right = r_mid

            print("r_left AFTER: ", r_left)
            print("r_right AFTER: ", r_right)
            print()

        return min(nums[l_ans], nums[r_ans])


if __name__ == "__main__":
    solution = Solution()

    q = [
        # ([3, 4, 5, 1, 2]),
        # ([4, 5, 6, 7, 0, 1, 2]),
        # ([11, 13, 15, 17]),
        # ([1]),
        # ([2, 1]),
        # ([2, 3, 4, 5, 1]),
        # ([3, 1, 2]),
        ([3, 4, 5, 6, 1, 2]),
    ]

    for nums in q:
        print("nums: ", nums)
        print()
        answer = solution.findMin(nums)
        print("answer: ", answer)
        print("=====================")
        print()
