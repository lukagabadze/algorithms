class Solution(object):
    def maxDifference(self, s: str) -> int:
        n = 26
        INF = float("inf")

        def ctn(c: str) -> int:
            return ord(c) - ord("a")

        def ntc(n: int) -> str:
            return

        cnts = [0] * n
        for c in s:
            cnts[ctn(c)] += 1

        max_odd = 0
        min_even = INF
        for i in range(26):
            if cnts[i] == 0:
                continue

            if cnts[i] % 2 == 0:
                min_even = min(min_even, cnts[i])
            else:
                max_odd = max(max_odd, cnts[i])

        return max_odd - min_even


if __name__ == "__main__":
    solution = Solution()

    q = [("aaaaabbc"), ("abcabcab"), ("tzt")]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.maxDifference(s)
        print("answer: ", answer)
        print("=====================")
        print()
