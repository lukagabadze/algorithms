class Solution(object):
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1

        left = 0
        right = x // 2 + 1
        while left < right:
            mid = (left + right) // 2
            sqr = mid * mid

            if sqr > x:
                right = mid
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    solution = Solution()

    q = [
        (4),
        (8),
        (50),
        (0),
        (1),
    ]

    for x in q:
        print("x: ", x)
        print()
        answer = solution.mySqrt(x)
        print("answer: ", answer)
        print("=====================")
        print()
