class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        # Turns even length palindromes into odd length palindromes for easy processing
        s = "#" + "#".join(s) + "#"

        n = len(s) // 2
        for i in range(n + 1):
            if s[n - i] != s[n + i]:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    # x = 121

    x = -121

    # x = 123321

    # x = 2

    print("x: ", x)
    print("\n")
    answer = solution.isPalindrome(x)
    print("\n")
    print("answer: ", answer)
