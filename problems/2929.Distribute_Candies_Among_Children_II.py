"""
TIME: 4017ms (Beats 17.81%)
NOTE: Looks like you can do this in 60ms time 😁.
I will be looking into that, meanwhile, I will enjoy the solution I came up with, even though its hella slow ❤️.
"""


class Solution(object):
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit * 3 == n:
            return 1

        if limit * 3 < n:
            return 0

        answer = 0
        for i in range(n + 1):
            # i is the first digit
            k = n - i

            if i > limit:
                continue

            if limit * 2 < k:
                continue

            if k == 0:
                answer += 1
                continue

            # Now we have 2 digit number to assemble with the same limit but with the sum of k
            two_digit_answer = (min(limit, k) - (k // 2)) * 2

            if k % 2 == 0:
                two_digit_answer += 1

            answer += two_digit_answer

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [(5, 2), (3, 3), (1, 2)]

    for n, limit in q:
        print("n: ", n)
        print("limit: ", limit)
        print()
        answer = solution.distributeCandies(n, limit)
        print("answer: ", answer)
        print("=====================")
        print()
