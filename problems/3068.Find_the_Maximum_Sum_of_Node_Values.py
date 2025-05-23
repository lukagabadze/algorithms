"""
NOTE: Thanks again to Sung Jinwoo for the solution!
(https://leetcode.com/problems/find-the-maximum-sum-of-node-values/solutions/6771396/greedy-xor-dp-with-images-example-walkthrough-c-python-java)

NOTE: This works because you can XOR any two nodes in this tree even if they are not "directly" connected.
The way you achieve this is by XOR-ing the path between these two nodes and as you go on the nodes you XOR-ed,
become un-XOR-ed, because "x ^ k ^ k = x". This is why going after largest gaining nodes works because you can XOR any two pairs of nodes.
So fucking cool.

NOTE: There are multiple ways to solve this, I need to look into other options.
"""

from typing import List


class Solution(object):
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum = 0
        gains = []
        for num in nums:
            sum += num
            gains.append((num ^ k) - num)

        gains.sort(reverse=True)

        for i in range(0, len(gains) - 1, 2):
            if gains[i] + gains[i + 1] <= 0:
                break

            sum += gains[i] + gains[i + 1]

        return sum


if __name__ == "__main__":
    solution = Solution()

    q = [
        ([1, 2, 1], 3, [[0, 1], [0, 2]]),
        ([2, 3], 7, [[0, 1]]),
        ([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]),
        ([1, 2, 3, 4, 5, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]),
    ]

    for nums, k, edges in q:
        print("nums: ", nums)
        print("k: ", k)
        print("edges: ", edges)
        print()
        answer = solution.maximumValueSum(nums, k, edges)
        print("answer: ", answer)
        print("=====================")
        print()
