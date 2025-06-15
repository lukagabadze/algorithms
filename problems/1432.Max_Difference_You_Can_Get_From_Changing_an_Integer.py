class Solution(object):
    def maxDiff(self, num: int) -> int:
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
        if s[0] == "1":
            i = 1
            while i < n and (s[i] == "0" or s[i] == "1"):
                i += 1
            if i != n:
                min_n = int(s.replace(s[i], "0"))
        else:
            min_n = int(s.replace(s[0], "1"))

        return max_n - min_n


if __name__ == "__main__":
    solution = Solution()

    q = [(555), (9), (99212399012221), (123456), (111)]

    for n in q:
        print("n: ", n)
        print()
        answer = solution.maxDiff(n)
        print("answer: ", answer)
        print("=====================")
        print()
