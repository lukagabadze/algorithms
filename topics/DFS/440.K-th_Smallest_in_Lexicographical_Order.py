"""
NOTE: Huge thanks to Priyanshu Pandey for the amazing explanation!
(https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/solutions/6825168/100-beat-count-children-skip-branches-o-log-n-well-explained-using-sparse-tree)

TODO: When I start the dfs from 1 the code does not work, i need to investigate why.
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return self.dfs(0, n, k)

    def dfs(self, current, n, k):
        # Base case, answer found
        if k == 0:
            return current // 10

        for i in range(max(current, 1), current + 10):
            size = self.subtree_size(i, i + 1, n)

            if size >= k:
                return self.dfs(i * 10, n, k - 1)

            # Getting closer to the answer
            k -= size

        # If none of the ranges was enough to get k to 0, it means k > n, which is impossible, so whatever
        return -1

    def subtree_size(self, current, neighbour, n):
        if neighbour > n:
            if current > n:
                return 0

            return n - current + 1

        # This recursion call goes wider and wider as it multiplies by 10
        # the left side goes more to the left, 1-10-100-1000-10000
        # and the right side goes more to the right, 9-90-900-9000-90000
        return (neighbour - current) + self.subtree_size(
            current * 10, neighbour * 10, n
        )


if __name__ == "__main__":
    solution = Solution()

    q = [(13, 2), (2, 1), (2000, 549)]

    for n, k in q:
        print("n: ", n)
        print("k: ", k)
        print()
        answer = solution.findKthNumber(n, k)
        print("answer: ", answer)
        print("=====================")
        print()
