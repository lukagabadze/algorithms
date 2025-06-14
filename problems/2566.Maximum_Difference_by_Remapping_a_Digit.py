class Solution(object):
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        n = len(s)

        # Max Logic
        max_n = num
        i = 0
        while i < n and s[i] == "9":
            i += 1

        if i != n:
            max_n = int(s.replace(s[i], "9"))

        # Min Logic
        min_n = num
        i = 0
        while i < n and s[i] == "0":
            i += 1

        if i != n:
            min_n = int(s.replace(s[i], "0"))

        return max_n - min_n


if __name__ == "__main__":
    solution = Solution()

    q = [
        (11891),
        (90),
        (99212399012221),
    ]

    for n in q:
        print("n: ", n)
        print()
        answer = solution.minMaxDifference(n)
        print("answer: ", answer)
        print("=====================")
        print()
