"""
NOTE: Thank you to the goat "cache_me_if_you_can" for the solution!
(https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/solutions/6815329/efficient-python-c-java-and-go-solutions)

I knew this was the solution but did not have enough time to implement it before the day was finished.
"""


class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)

        # Create suffix min map
        min_map = [""] * n
        min_c = "z"
        for i in reversed(range(n)):
            min_c = min(min_c, s[i])
            min_map[i] = min_c

        t, p, i = [], [], 0
        while i < n:
            # Try accumulated target string first for min chars
            while t and t[-1] <= min_map[i]:
                p.append(t.pop())

            # Afer completing the target string, insert a character from s into target
            t.append(s[i])

            i += 1

        # Flush the target
        while t:
            p.append(t.pop())

        return "".join(p)


if __name__ == "__main__":
    solution = Solution()

    q = [
        ("zza"),
        ("bac"),
        ("bdda"),
    ]

    for s in q:
        print("s: ", s)
        print()
        answer = solution.robotWithString(s)
        print("answer: ", answer)
        print("=====================")
        print()
