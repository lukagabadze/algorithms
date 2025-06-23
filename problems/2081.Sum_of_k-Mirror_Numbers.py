"""
NOTE: HUGE thanks to varma_5247 for the solution!
(https://leetcode.com/problems/sum-of-k-mirror-numbers/solutions/6873949/beginner-freindly-java-c-python)

I was cooked today so not much effort went into solving this on my own...
"""


class Solution(object):
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10

        while x > 0:
            num = num * 10 + x % 10
            x //= 10

        return num

    def isPalindrome(self, n: int, k: int) -> bool:
        digits = []
        while n > 0:
            digits.append(n % k)
            n //= k

        return digits == digits[::-1]

    def kMirror(self, k: int, n: int) -> int:
        answer = 0
        length = 1
        while n > 0:
            # Even lengths
            for i in range(length, length * 10):
                if n <= 0:
                    break

                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    answer += p
                    n -= 1

            # Odd lengths
            for i in range(length, length * 10):
                if n <= 0:
                    break

                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    answer += p
                    n -= 1

            length *= 10

        return answer


if __name__ == "__main__":
    solution = Solution()

    q = [
        (2, 5),
        (3, 7),
        (7, 17),
    ]

    for k, n in q:
        print("k: ", k)
        print("n: ", n)
        print()
        print()
        answer = solution.kMirror(k, n)
        print("answer: ", answer)
        print("=====================")
        print()
